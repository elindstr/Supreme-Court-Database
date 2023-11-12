# Supreme-Court-Database
A complete database of all decisions by the United States Supreme Court.

## Code Description

"01_scrape.py" is a python script that downloads to text files the complete set of Supreme Court decisions published in the [United States Reports](https://en.wikipedia.org/wiki/United_States_Reports) as hosted on [Justia.com](https://supreme.justia.com/cases/federal/us/volume/).

output file size: ~836 MB
runtime: ~4.5 hours

## Database Information

The [United States Reports](https://en.wikipedia.org/wiki/United_States_Reports) has been the official reporter of Supreme Court decisions since 1874. Decisions before 1874 were republished as U.S. Reports volumes 1 through 90. Decisions issued in 2023 are expected to be published in volume 600, although the pagination of recent volumes take several years to finalize.  

Before 1874, Supreme Court decisions were reported in a series of publications named for private publishers. The first publication, "Dallas Reports," actually predates the Supreme Court itself. "Dallas Reports" consists of four volumes spanning decision from 1754 to 1800, including decisions by the Supreme Court <i>and other courts</i>. Indeed, Dallas Reports volume 1 contains entirely cases predating the Supreme Court; the first Supreme Court decision, <i>West v. Barnes</i> (1791), doesn't appear until near the end of Dallas Report volume 2. Nevertheless, when the U.S. Reports was retroactively numbered in 1874, Dallas Reports volumes 1 through 4 were republished as U.S. Reports volumes 1 through 4.

"01_scrape.py" crawls through the U.S Reports as hosted by Justia iteratively by volume. Data.zip consists of U.S Reports volumes 3 through 600. I manually added the Supreme Court decision published at the end of U.S. Reports volume 2. I did not remove non-Supreme Court decisions included in volumes 3 and 4.

Decisions are saved as [UTF-8](https://en.wikipedia.org/wiki/UTF-8) text files. Files are scraped as printed by U.S. Reports according to Justia, and in addition "01_scrape.py" writes 6 lines of metadata to the beginning of each file, populated where such information is available, e.g.:

    ::decision_cite:: 539 U.S. 558 (2003)
    ::decision_name::  Lawrence v. Texas
    ::decision_year:: 2003
    ::opinion_author:: 
    ::opinion_type:: 
    ::opinion:: 

"01_scrape.py" titles most text files as '[citation] + [decision_name] + [opinion_type] (when available) + [opinion_author] (when available)'. Recently, Justia's database includes different pages for decisions with multiple opinions by different justices, so the opinion_type and opinion_author are included to prevent file over-writing. Older decision in Justia's database included concurrences and dissents on the same page. "01_scrape.py" makes no attempt to merge or separate multi-opinion decisions different that as hosted by Justia. 

Because very recent volumes of U.S. Reports do not have finalized pagination (since volume 575), citations in the file names refer to Supreme Court [Docket Number](http://scdb.wustl.edu/documentation.php?var=docket).

I have documented a few issues with the Justia database:

1. Justia's U.S. Reports volume 2 directory appears incomplete. So I supplemented apparently missing Justia data with decisions hosted on [Wikisource](https://en.wikisource.org/wiki/United_States_Reports/Volume_2).

2. There is one Justia case page with no opinion content: https://supreme.justia.com/cases/federal/us/585/141-orig/; although this decision is an unusual report by a special master. I located this decision in another database (https://en.wikisource.org/wiki/United_States_Reports/Volume_2) and included those decisions in mine.

3. At least one Justia case has no U.S Reports metadata: Republican National Committee v. Democratic National Committee (2020): https://supreme.justia.com/cases/federal/us/589/19a1016/. 

## Copyright Information

The Supreme Court publishes its decisions to the public domain and the Court has specifically held that volumes of U.S. Reports are not copyrightable. <i>Wheaton v. Peters</i>, 33 U.S. 591, 668 (1834) ("no reporter has or can have any copyright in the written opinions delivered by this Court"). The Court has also held that compilations of factual information, like the white pages of a telephone book, are not copyrightable absent creative additions like a curated selection or annotated comment. <i>Feist Publications, Inc. v. Rural Telephone Service Co.</i>, 499 U. S. 340 (1991)</sup>.

## License

MIT
