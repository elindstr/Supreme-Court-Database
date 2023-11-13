# Supreme-Court-Database

A script to download all decisions by the United States Supreme Court.

## Code Description

"scrape.py" is a python script that downloads to text files the complete set of Supreme Court decisions published in the [United States Reports](https://en.wikipedia.org/wiki/United_States_Reports). Decisions are scraped from public domain content on [Wikisource.com](https://en.wikisource.org/wiki/United_States_Reports/Volume_2) and [Justia.com](https://supreme.justia.com/cases/federal/us/volume/). (See copyright note section [below](#copyright-information).)

Statistics:
* output files: 33,627
* output file size: ~835 MB
* runtime: ~4.5 hours

## Database Information
 
U.S. Reports is the official reporter of Supreme Court decisions. Congress didn't create U.S. Reports until 1874, but the publication retroactively published 90 volumes of decisions back to the Court's first orders in 1790. 

Decisions before 1874 were reported in volumes by a series of quasi-official private publishers. The first Supreme Court decisions were included in "Dallas Reports," a publication that predated the Supreme Court, and Supreme Court decisions were published alongside decisions from other courts. Beginning in 1801, Supreme Court decisions were published in stand-alone volumes. In 1874, U.S. Reports adopted the volume numbering and organization of the previous publishers, included the entirety of the Dallas Reports with its decisions from other courts. Indeed, U.S. Reports volume 1 doesn't contain any Supreme Court decisions; the first Supreme Court decision, <i>West v. Barnes</i> (1791), doesn't appear until near the end of U.S Reports (Dallas Reports) volume 2.

Modernly, U.S. Reports publishes decisions from each court term in volumes that are around 1,000 pages. Final pagination is not established for several years after decisions are issued, during which changes the decisions themselves is still possible.<sup>[1](#note_1)</sup> Thus, while citation to the U.S. Reports volume and page number is the standard citation in legal writing, very recent decisions do not yet have a U.S. Reports page number and must be cited in other ways.    

"scrape.py" crawls U.S Reports iteratively by volume beginning with the first Supreme Decisions near the end of volume 2, scraping each decision as hosted by [Wikisource.com](https://en.wikisource.org/wiki/United_States_Reports/Volume_2) and [Justia.com](https://supreme.justia.com/cases/federal/us/volume/). Other than beginning at the end of volume 2, "scrape.py" makes no effort to remove the non-Supreme Court decisions in volumes 3 and 4.

Decisions are saved as [UTF-8](https://en.wikipedia.org/wiki/UTF-8) text files. "scrape.py" writes 6 lines of metadata to the beginning of each file, populated where such information is available:

    ::decision_cite:: 539 U.S. 558 (2003)
    ::decision_name:: Lawrence v. Texas
    ::decision_year:: 2003
    ::opinion_author:: 
    ::opinion_type:: 
    ::opinion:: 

Some Supreme Court decisions consist of one majority opinion, written either by the Court as a whole (<i>per curiam</i>) or by a single justice. Other decisions have multiple opinions, with one or more justice writing separately in concurrence or dissent. Justia publishes historic decisions with all opinions consecutively on the same page; "scrape.py" scrapes these pages into one file. Modernly, Justia has begun separating decisions with multiple opinions into separate webpages (or hidden divs); "scrape.py" scrapes these opinions into different files.

"scrape.py" titles most text files as '[citation] + [decision_name] + [opinion_type] (when available) + [opinion_author] (when available)'. Because very recent volumes of U.S. Reports do not have finalized pagination (since volume 575), "scrape.py" titles these decisions using their the Supreme Court [Docket Number](http://scdb.wustl.edu/documentation.php?var=docket).

I have documented a few issues with the Justia database:

1. Justia's U.S. Reports volume 2 directory is incomplete, so "scrape.py" supplements the missing decisions from [Wikisource](https://en.wikisource.org/wiki/United_States_Reports/Volume_2).

2. There is one Justia case page with no opinion content (https://supreme.justia.com/cases/federal/us/585/141-orig/), although this decision is an unusual report by a special master. 

3. At least one Justia case has no U.S Reports metadata: Republican National Committee v. Democratic National Committee (2020): https://supreme.justia.com/cases/federal/us/589/19a1016/. 

<a name="note_1"></a><sup><sup>1</sup> Richard J. Lazarus, "[The (Non)Finality of Supreme Court Opinions](https://harvardlawreview.org/print/vol-128/the-nonfinality-of-supreme-court-opinions/)," 128 Harv. L. Rev. 540 (2014).</sup>

## Copyright Information

The Supreme Court publishes its decisions to the public domain and the Court has specifically held that volumes of U.S. Reports are not copyrightable. <i>Wheaton v. Peters</i>, 33 U.S. 591, 668 (1834) ("no reporter has or can have any copyright in the written opinions delivered by this Court"). The Court has also held that compilations of factual information, like the white pages of a telephone book, are not copyrightable absent creative additions like a curated selection or annotated comment. <i>Feist Publications, Inc. v. Rural Telephone Service Co.</i>, 499 U. S. 340 (1991)</sup>.

## License

MIT
