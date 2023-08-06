import re
import nbformat
from nbformat.v4.nbbase import new_markdown_cell
import itertools
import json

from .config import *

class Nb:

    # markdown link returning txt and url groups
    MD_LINK = re.compile(r'(?:[^!]\[(?P<txt>.*?)\]\((?P<url>.*?)\))')

    # markdown figure returning txt and url groups
    MD_FIG = re.compile(r'(?:!\[(?P<txt>.*?)\]\((?P<url>.*?)\))')

    # html image tag
    HTML_IMG = re.compile(r'<img[^>]*>')

    # markdown header
    MD_HEADER = re.compile(r'(^|\n)(?P<level>#{1,6})(?P<header>.*?)#*(\n|$)')

    def __init__(self, filename, chapter, section):
        self.filename = filename
        self.path = os.path.join(NOTEBOOK_DIR, filename)
        self.chapter = chapter
        self.section = section
        self.url = os.path.join(NBVIEWER_URL, filename)
        self.colab_link = COLAB_LINK.format(notebook_filename=os.path.basename(self.filename))
        self.content = nbformat.read(self.path, as_version=4)
        self.navbar = None

    @property
    def title(self):
        """Return the tile of a notebook obtained from the first level one header."""
        for cell in self.content.cells:
            if cell.cell_type == "markdown":
                m = self.__class__.MD_HEADER.match(cell.source)
                if m and len(m.group('level')) == 1:
                    return m.group('header').strip()
        return None

    @property
    def figs(self):
        """Return a list of markdown figures appearing in a notebook."""
        figs = []
        for cell in self.content.cells:
            if cell.cell_type == "markdown":
                figs.extend(self.__class__.MD_FIG.findall(cell.source))
        return figs

    @property
    def links(self):
        """Return a list of markdown links appearing in a notebook."""
        links = []
        for cell in self.content.cells[2:-1]:
            if cell.cell_type == "markdown":
                links.extend(self.__class__.MD_LINK.findall(cell.source))
        return links

    @property
    def imgs(self):
        """Return a list of html img tags appearing in a notebook."""
        imgs = []
        for cell in self.content.cells[2:-1]:
            if cell.cell_type == "markdown":
                imgs.extend(self.__class__.HTML_IMG.findall(cell.source))
        return imgs

    @property
    def link(self):
        """Return a markdown link to the public html view of a notebook."""
        return f"[{self.numbered_title}]({self.url})"

    @property
    def readme(self):
        """Return formatted entry for this notebook in the repository readme file."""
        return "\n### " + self.link

    @property
    def toc(self):
        """Return formmatted list of markdown links to cells starting with a markdown header."""
        toc = []
        header_cells = (cell for cell in self.content.cells if cell.cell_type == "markdown" and cell.source.startswith("##"))
        for header_cell in header_cells:
            header = header_cell.source.splitlines()[0].strip().split()
            txt = ' '.join(header[1:])
            url = '#'.join([self.url, '-'.join(header[1:])])
            toc.append("    "*(len(header[0])-2) + f"- [{txt}]({url})")
        return toc

    @property
    def keyword_index(self):
        "Return keyword index and links for a notebook."
        index = dict()
        headercells = (cell for cell in self.content.cells if cell.cell_type == "markdown" and cell.source.startswith("#"))
        for headercell in headercells:
            lines = headercell.source.splitlines()
            header = lines[0].strip().split()
            txt = ' '.join(header[1:])
            url = '#'.join([self.url, '-'.join(header[1:])])
            for keywordline in [line.strip() for line in lines[1:] if line.lower().startswith("keywords: ")]:
                for word in keywordline.split(':')[1].split(','):
                    index.setdefault(word.strip(), []).append(f"[{txt}]({url})")
        return index

    @property
    def orphan_headers(self):
        """"Return a list of orphan headers in a notebook."""
        orphans = []
        for cell in self.content.cells[2:-1]:
            if cell.cell_type == "markdown":
                 for line in cell.source.splitlines()[1:]:
                     if self.__class__.MD_HEADER.match(line):
                         orphans.append(line)
        return orphans

    def write_navbar(self):
        """Insert navigation bar into a notebook."""
        if self.content.cells[1].source.startswith(NAVBAR_TAG):
            print(f"- amending navbar for {self.filename}")
            self.content.cells[1].source = self.navbar
        else:
            print(f"- inserting navbar for {self.filename}")
            self.content.cells.insert(1, new_markdown_cell(source=self.navbar))
        if self.content.cells[-1].source.startswith(NAVBAR_TAG):
            print(f"- amending navbar for {self.filename}")
            self.content.cells[-1].source = self.navbar
        else:
            print(f"- inserting navbar for {self.filename}")
            self.content.cells.append(new_markdown_cell(source=self.navbar))
        nbformat.write(self.content, self.path)

    def __gt__(self, nb):
        return self.filename > nb.filename

    def __str__(self):
        return self.filename


class FrontMatter(Nb):
    def __init__(self, filename, chapter, section):
        super().__init__(filename, chapter, section)

    @property
    def numbered_title(self):
        """Return formatted title with numbering for a notebook."""
        return f"{self.title}"

    @property
    def toc(self):
        """Return table of contents entry for a notebook."""
        toc = Nb.toc.fget(self)
        toc.insert(0, "\n## " + self.link)
        return toc


class Chapter(Nb):
    def __init__(self, filename, chapter, section):
        super().__init__(filename, chapter, section)

    @property
    def numbered_title(self):
        """Return formatted title with numbering for a notebook."""
        return f"Chapter {int(self.chapter)}.{int(self.section)} {self.title}"

    @property
    def toc(self):
        """Return table of contents entry for a notebook."""
        toc = Nb.toc.fget(self)
        toc.insert(0, "\n## " + self.link)
        return toc


class Appendix(Nb):
    def __init__(self, filename, chapter, section):
        super().__init__(filename, chapter, section)

    @property
    def numbered_title(self):
        """Return formatted title with numbering for a notebook."""
        return f"Appendix {self.chapter}. {self.title}"

    @property
    def toc(self):
        """Return table of contents entry for a notebook."""
        toc =  Nb.toc.fget(self)
        toc.insert(0, "\n## " + self.link)
        return toc


class Section(Nb):
    def __init__(self, filename, chapter, section):
        super().__init__(filename, chapter, section)

    @property
    def readme(self):
        """Return formatted entry for this notebook in the repository readme file."""
        return "- " + self.link

    @property
    def numbered_title(self):
        """Return formatted title with numbering for a notebook."""
        try:
            return f"{int(self.chapter)}.{int(self.section)} {self.title}"
        except:
            return f"{self.chapter}.{int(self.section)} {self.title}"

    @property
    def toc(self):
        """Return table of contents entry for a notebook."""
        toc =  Nb.toc.fget(self)
        toc.insert(0, "### " + self.link)
        return toc


class NbHeader:

    NOTEBOOK_HEADER_TAG = "<!--NOTEBOOK_HEADER-->"

    def __init__(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('notebook_header.jinja')
        self.content = template.render(page_title=PAGE_TITLE, page_url=PAGE_URL, github_url=GITHUB_URL)
        self.source = self.__class__.NOTEBOOK_HEADER_TAG + self.content

    def write(self, nb):
        """
        Write header to a notebook file.
        :param nb: notebook object
        """
        if nb.content.cells[0].source.startswith(self.__class__.NOTEBOOK_HEADER_TAG):
            print('- amending header for {0}'.format(nb.filename))
            nb.content.cells[0].source = self.source
        else:
            print('- inserting header for {0}'.format(nb.filename))
            nb.content.cells.insert(0, new_markdown_cell(self.source))

        nbformat.write(nb.content, nb.path)


class NbCollection:
    # regular expression that matches notebook filenames to be included in the TOC
    REG = re.compile(r'(\d\d|[A-Z])\.(\d\d)-(.*)\.ipynb')

    def __init__(self, dir=NOTEBOOK_DIR):
        self.notebooks = []
        for filename in sorted(os.listdir(dir)):
            if self.__class__.REG.match(filename):
                chapter, section, _ = self.__class__.REG.match(filename).groups()
                if section not in "00":
                    self.notebooks.append(Section(filename, chapter, section))
                elif chapter in "00":
                    self.notebooks.append(FrontMatter(filename, chapter, section))
                elif chapter.isdigit():
                    self.notebooks.append(Chapter(filename, chapter, section))
                else:
                    self.notebooks.append(Appendix(filename, chapter, section))
        self.nbheader = NbHeader()
        self._keyword_index = {}

    @property
    def keyword_index(self):
        """Return keyword dictionary with list of links for a collection of notebooks."""
        # use self._keyword_index to cache results
        if not self._keyword_index:
            for nb in self.notebooks:
                for word, links in nb.keyword_index.items():
                    for link in links:
                        self._keyword_index.setdefault(word, []).append(link)
        return self._keyword_index

    def write_headers(self):
        """Insert a common header into a collection of notebooks."""
        for nb in self.notebooks:
            self.nbheader.write(nb)

    def write_navbars(self):
        """Insert navigation bars into a collection of notebooks."""
        if self.notebooks:
            a, b, c = itertools.tee(self.notebooks, 3)
            next (c)
            for prev_nb, nb, next_nb in zip(itertools.chain([None], a), b, itertools.chain(c, [None])):
                nb.navbar = NAVBAR_TAG
                nb.navbar += PREV_TEMPLATE.format(title=prev_nb.title, url=prev_nb.url) if prev_nb else ''
                nb.navbar += CONTENTS + INDEX if self.keyword_index else CONTENTS
                nb.navbar += NEXT_TEMPLATE.format(title=next_nb.title, url=next_nb.url) if next_nb else ''
                nb.navbar += nb.colab_link
                nb.write_navbar()

    def write_toc(self):
        """Write table of contents file for a collection of notebooks."""
        print("- writing table of contents file")
        with open(TOC_FILE, 'w') as f:
            print(TOC_HEADER, file=f)
            for nb in self.notebooks:
                f.write('\n')
                f.write('\n'.join(nb.toc) + '\n')
                if nb.figs:
                    print("* Figures", file=f)
                    for txt, url in nb.figs:
                        print("    - [{0}]({1})".format(txt if txt else url, url), file=f)
                if nb.links:
                    print("* Links", file=f)
                    for txt, url in nb.links:
                        print(f"    - [{txt}]({url})", file=f)
        os.system(' '.join(['notedown', f'"{TOC_FILE}"', '>', f'"{TOC_NB}"']))

    def write_keyword_index(self):
        """Write keyword index file for a collection of notebooks."""
        keywords = sorted(self.keyword_index.keys(), key=str.lower)
        print("- writing keyword index file")
        with open(INDEX_FILE, 'w') as f:
            print(INDEX_HEADER, file=f)
            if keywords:
                print("\n## Keyword Index", file=f)
                f.write("\n")
                for keyword in keywords:
                    f.write("* " + keyword + "\n")
                    for link in self.keyword_index[keyword]:
                        f.write("    - " + link + "\n")
        os.system(' '.join(['notedown', f'"{INDEX_FILE}"', ">", f'"{INDEX_NB}"']))

    def write_readme(self):
        """Write README.md using readme.md.jinja."""
        print("- writing README.md")
        readme_toc = [README_TOC] if self.notebooks else []
        readme_toc += [README_INDEX] if self.keyword_index.keys() else []
        readme_toc += [nb.readme for nb in self.notebooks]
        env = Environment(loader=FileSystemLoader('templates'))
        with open(README_FILE, 'w') as f:
            f.write(env.get_template('README.md.jinja').render(readme_toc=readme_toc, page_title=PAGE_TITLE, github_url=GITHUB_URL))

    def lint(self):
        """Search for and report style issues in a collection of notebooks."""
        for nb in self.notebooks:
            if nb.imgs:
                print("\n", nb.filename)
                for img in nb.imgs:
                    print(img)
            if nb.orphan_headers:
                print("\nOrphan headers in ", nb.filename)
                for orphan in nb.orphan_headers:
                    print(orphan)

    def metadata(self):
        """Print metadata for a collection of notebooks."""
        for nb in self.notebooks:
            print(json.dumps(nb.content['metadata'], sort_keys=True, indent=4))
