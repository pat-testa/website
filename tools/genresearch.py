"""One-shot generator for research/index.qmd.

Emits the page with Abstract / BibTeX toggles. Abstracts come from
abstracts.json (extracted from the PDFs); citations and BibTeX are written
by hand here, with DOIs verified against Crossref. After running this once
the .qmd is a normal hand-editable file.
"""
import json, html

ABS = json.load(open("abstracts.json"))

A = {  # coauthor links
 "bazzi":"[Samuel Bazzi](https://sites.google.com/site/samuelbazzi/)",
 "ferrara":"[Andreas Ferrara](http://andreas-ferrara.com/)",
 "fiszbein":"[Martin Fiszbein](https://sites.google.com/site/martinfiszbein/)",
 "pearson":"[Thomas Pearson](https://sites.google.com/view/thomaspearson)",
 "skaperdas":"[Stergios Skaperdas](https://scholar.google.com/citations?user=IXHHwT0AAAAJ&hl=en)",
 "williams":"[Jhacova Williams](https://www.american.edu/spa/faculty/jhacovaw.cfm)",
 "zhou":"[Liyang Zhou](https://www.econ.pitt.edu/people/liyang-zhou)",
 "chyn":"[Eric Chyn](https://www.ericchyn.com/)",
 "alster":"[Grace Alster](https://economics.ucsd.edu/graduate-program/about/grad-profiles/cohort-2023/alster-grace.html)",
 "zivin":"[Joshua Graff Zivin](https://www.joshgraffzivin.com/)",
}

def bib(key, author, title, journal, year, volume=None, pages=None, doi=None,
        note=None, kind="article"):
    L=[f"  author  = {{{author}}}", f"  title   = {{{title}}}"]
    if journal: L.append(f"  journal = {{{journal}}}")
    L.append(f"  year    = {{{year}}}")
    if volume: L.append(f"  volume  = {{{volume}}}")
    if pages:  L.append(f"  pages   = {{{pages}}}")
    if doi:    L.append(f"  doi     = {{{doi}}}")
    if note:   L.append(f"  note    = {{{note}}}")
    return "@%s{%s,\n%s\n}" % (kind, key, ",\n".join(L))

WORKING = [dict(
  slug="elections-political-investment",
  cite='"Elections and Political Investment."',
  links='Download: [Draft (with appendices)](../files/elections-political-investment.pdf).',
  summary='Beyond selecting officeholders and policies, election results help inform political actors where to invest their time and resources.',
  bibtex=bib("testa2026elections","Testa, Patrick A.","Elections and Political Investment",
             None,2026,note="Working paper",kind="unpublished"),
)]

PUBS = [
 dict(slug="confederate-diaspora",
   cite=f'"[The Confederate Diaspora](https://www.restud.com/the-confederate-diaspora/)" (with {A["bazzi"]}, {A["ferrara"]}, {A["fiszbein"]}, and {A["pearson"]}), forthcoming at the *Review of Economic Studies*.',
   links='Download: [Draft](../files/confederate-diaspora.pdf), [Supplemental material](../files/confederate-diaspora-supplement.pdf), [Replication files](https://zenodo.org/records/17361408).',
   summary='Former Confederate elites moved West after the Civil War, migrating into positions of power and shaping the trajectory of American culture.',
   bibtex=bib("bazzi2026confederate","Bazzi, Samuel and Ferrara, Andreas and Fiszbein, Martin and Pearson, Thomas and Testa, Patrick A.",
              "The Confederate Diaspora","Review of Economic Studies",2026,
              doi="10.1093/restud/rdag027", note="Forthcoming")),

 dict(slug="state-capacity-identity",
   cite=f'"[State Capacity and Identity: Assimilation vs. Resistance of Tribal Rimlands](https://www.sciencedirect.com/science/article/pii/S0014292126000164)," *European Economic Review*, 2026, 184, 105272 (with {A["skaperdas"]}). Part of a Virtual Special Issue on the Legacy of James C. Scott.',
   links='Download: [Draft (with appendices)](../files/state-capacity-identity.pdf).',
   summary='The persistence of subnational identities during nation building depends on state capacity as well as tribal resistance strategies.',
   bibtex=bib("skaperdas2026state","Skaperdas, Stergios and Testa, Patrick A.",
              "State Capacity and Identity: Assimilation vs. Resistance of Tribal Rimlands",
              "European Economic Review",2026,volume="184",pages="105272",
              doi="10.1016/j.euroecorev.2026.105272")),

 dict(slug="racial-violence",
   cite=f'"[Political Foundations of Racial Violence in the Post-Reconstruction South](https://academic.oup.com/qje/advance-article-abstract/doi/10.1093/qje/qjaf045/8248520)," *Quarterly Journal of Economics*, 2026, 141, 733–49 (with {A["williams"]}).',
   links='Download: [Draft](../files/racial-violence.pdf), [Supplemental material](../files/racial-violence-supplement.pdf).',
   summary='Racial violence in the post-Reconstruction U.S. South was closely tied to the local political performance of the Democratic Party.',
   bibtex=bib("testa2026political","Testa, Patrick A. and Williams, Jhacova",
              "Political Foundations of Racial Violence in the Post-Reconstruction South",
              "Quarterly Journal of Economics",2026,volume="141",pages="733--749",
              doi="10.1093/qje/qjaf045")),

 dict(slug="national-identity",
   cite=f'"[National Identity, Public Goods, and Modern Economic Development](https://www.sciencedirect.com/science/article/pii/S014759672500006X)," *Journal of Comparative Economics*, 2025, 53, 412–32 (with {A["skaperdas"]}).',
   links='Download: [Draft (with appendices)](../files/national-identity.pdf).',
   summary='National identities promote a consensus between elites and the masses behind taxes and public goods that boost the national economic status, further galvanizing national pride.',
   bibtex=bib("skaperdas2025national","Skaperdas, Stergios and Testa, Patrick A.",
              "National Identity, Public Goods, and Modern Economic Development",
              "Journal of Comparative Economics",2025,volume="53",pages="412--432",
              doi="10.1016/j.jce.2025.01.006")),

 dict(slug="crosswalks",
   cite=f'"[New Area- and Population-based Geographic Crosswalks for U.S. Counties and Congressional Districts, 1790-2020](https://www.tandfonline.com/doi/full/10.1080/01615440.2024.2369230)," *Historical Methods*, 2024, 57, 67–79 (with {A["ferrara"]} and {A["zhou"]}).',
   links='Download: [Draft](../files/crosswalks.pdf), [Supplemental material](../files/crosswalks-supplement.pdf), [Crosswalks and replication files](https://doi.org/10.3886/E150101).',
   summary='We develop new geographic crosswalks for the U.S. based on relative population size, which account for heterogeneities in urbanization within counties.',
   bibtex=bib("ferrara2024new","Ferrara, Andreas and Testa, Patrick A. and Zhou, Liyang",
              "New Area- and Population-based Geographic Crosswalks for {U.S.} Counties and Congressional Districts, 1790--2020",
              "Historical Methods",2024,volume="57",pages="67--79",
              doi="10.1080/01615440.2024.2369230")),

 dict(slug="other-great-migration",
   cite=f'"[The Other Great Migration: Southern Whites and the New Right](https://academic.oup.com/qje/advance-article/doi/10.1093/qje/qjad014/7080180)," *Quarterly Journal of Economics*, 2023, 138, 1577–1647 (with {A["bazzi"]}, {A["ferrara"]}, {A["fiszbein"]}, and {A["pearson"]}).',
   links='Download: [Draft](../files/other-great-migration.pdf), [Supplemental material](../files/other-great-migration-supplement.pdf), [Replication files](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KLIPEM).',
   summary='Mass migration out of the U.S. South during the early 20th century catalyzed major shifts in national policy coalitions.',
   bibtex=bib("bazzi2023other","Bazzi, Samuel and Ferrara, Andreas and Fiszbein, Martin and Pearson, Thomas and Testa, Patrick A.",
              "The Other Great Migration: Southern Whites and the New Right",
              "Quarterly Journal of Economics",2023,volume="138",pages="1577--1647",
              doi="10.1093/qje/qjad014")),

 dict(slug="churches-social-insurance",
   cite=f'"[Churches as Social Insurance: Oil Risk and Religion in the U.S. South](https://www.cambridge.org/core/journals/journal-of-economic-history/article/churches-as-social-insurance-oil-risk-and-religion-in-the-us-south/8CA18A5677CA71539DD7D604D38C2F75)," *Journal of Economic History*, 2023, 83, 786–832 (with {A["ferrara"]}).',
   links='Download: [Draft](../files/churches-social-insurance.pdf), [Supplemental material](../files/churches-social-insurance-supplement.pdf), [Replication files](https://www.openicpsr.org/openicpsr/project/179761/version/V1/view).',
   summary='Religious communities grew throughout the U.S. South in the early 20th century as a form of social insurance against oil volatility.',
   bibtex=bib("ferrara2023churches","Ferrara, Andreas and Testa, Patrick A.",
              "Churches as Social Insurance: Oil Risk and Religion in the {U.S.} South",
              "Journal of Economic History",2023,volume="83",pages="786--832",
              doi="10.1017/S0022050723000268")),

 dict(slug="sundown-towns",
   cite=f'"[Sundown Towns and Racial Exclusion: The Southern White Diaspora and the \'Great Retreat\'](https://www.aeaweb.org/articles?id=10.1257/pandp.20221104)," *American Economic Association: Papers and Proceedings*, 2022, 112, 234–8 (with {A["bazzi"]}, {A["ferrara"]}, {A["fiszbein"]}, and {A["pearson"]}).',
   links='Download: [Draft](../files/sundown-towns.pdf), [Replication files](https://www.openicpsr.org/openicpsr/project/164162/version/V1/view).',
   summary='Racially-exclusive "sundown towns" spread throughout the central and western U.S. in the 1900s, leading to a "Great Retreat" of Black Americans.',
   bibtex=bib("bazzi2022sundown","Bazzi, Samuel and Ferrara, Andreas and Fiszbein, Martin and Pearson, Thomas and Testa, Patrick A.",
              "Sundown Towns and Racial Exclusion: The Southern White Diaspora and the ``Great Retreat''",
              "AEA Papers and Proceedings",2022,volume="112",pages="234--238",
              doi="10.1257/pandp.20221104")),

 dict(slug="expulsion-czechoslovakia",
   cite='"[The Economic Legacy of Expulsion: Lessons from Post-war Czechoslovakia](https://academic.oup.com/ej/article/131/637/2233/6021415)," *The Economic Journal*, 2021, 131, 2233–71.',
   links='Download: [Draft](../files/expulsion-czechoslovakia.pdf), [Supplemental material](../files/expulsion-czechoslovakia-supplement.pdf), [Replication files](https://drive.google.com/file/d/1KHnC7Q8zT9l6DbE11zDFqH-KQaBYCSwq/view?usp=sharing).',
   summary="Czechoslovakia's expulsion of millions of ethnic Germans after World War II permanently impaired local economic development.",
   bibtex=bib("testa2021economic","Testa, Patrick A.",
              "The Economic Legacy of Expulsion: Lessons from Post-war Czechoslovakia",
              "The Economic Journal",2021,volume="131",pages="2233--2271",
              doi="10.1093/ej/ueaa132")),

 dict(slug="shocks-spatial-distribution",
   cite='"[Shocks and the Spatial Distribution of Economic Activity: The Role of Institutions](https://www.sciencedirect.com/science/article/pii/S0167268120303899)," *Journal of Economic Behavior & Organization*, 2021, 183, 791–810.',
   links='Download: [Draft](../files/shocks-spatial-distribution.pdf), [Supplemental material](../files/shocks-spatial-distribution-supplement.pdf), [Replication files](https://drive.google.com/file/d/1snNFKSm1MzzyTRO2YMJqrWMeOgNAWx5b/view?usp=sharing).',
   summary='When it comes to whether or not historical shocks have persistent effects, the quality of institutions matters for migratory responses.',
   bibtex=bib("testa2021shocks","Testa, Patrick A.",
              "Shocks and the Spatial Distribution of Economic Activity: The Role of Institutions",
              "Journal of Economic Behavior \\& Organization",2021,volume="183",pages="791--810",
              doi="10.1016/j.jebo.2020.10.021")),

 dict(slug="education-propaganda",
   cite='"[Education and Propaganda: Tradeoffs to Public Education Provision in Nondemocracies](https://www.sciencedirect.com/science/article/abs/pii/S0047272718300410)," *Journal of Public Economics*, 2018, 160, 66–81.',
   links='Download: [Draft](../files/education-propaganda.pdf), [Supplemental material](../files/education-propaganda-supplement.pdf), [Replication files](https://drive.google.com/open?id=12o8UA2O3An2Lnfe5Mxy8abX6jx9evfVb).',
   summary='The use of propaganda in educational content can induce nondemocracies to invest more in education, ultimately making citizens better off.',
   bibtex=bib("testa2018education","Testa, Patrick A.",
              "Education and Propaganda: Tradeoffs to Public Education Provision in Nondemocracies",
              "Journal of Public Economics",2018,volume="160",pages="66--81",
              doi="10.1016/j.jpubeco.2018.03.001")),
]

def entry(p):
    out=["::: {.entry}", p["cite"], "", f'[{p["links"]}]{{.links}}', "",
         f'[Summary: {p["summary"]}]{{.summary}}', ""]
    a, s = ABS.get(p["slug"]), p["slug"]
    pills, panels = [], []
    if a:
        pills.append(f'<button class="pill" type="button" aria-expanded="false" '
                     f'aria-controls="abs-{s}">Abstract</button>')
        panels.append(f'<div class="panel" id="abs-{s}" hidden>{html.escape(a)}</div>')
    pills.append(f'<button class="pill" type="button" aria-expanded="false" '
                 f'aria-controls="bib-{s}">BibTeX</button>')
    panels.append(f'<div class="panel" id="bib-{s}" hidden>'
                  f'<button class="copy-bib" type="button">Copy</button>'
                  f'<pre><code>{html.escape(p["bibtex"])}</code></pre></div>')
    out.append('<div class="actions">' + "".join(pills) + '</div>')
    out.append('<div class="panels">' + "".join(panels) + '</div>')
    out += [':::', '']
    return "\n".join(out)

doc = ['---','title: "Research"','---','','## Research statement','',
       '[Download](../files/research-statement.pdf).','','## Working papers','']
for p in WORKING: doc.append(entry(p))
doc += ['## Publications','']
for p in PUBS: doc.append(entry(p))
doc += ['## Selected work in progress','',
 '::: {.entry}',
 f'"The Geography of Demographic Composition in the United States" (with {A["bazzi"]}, {A["chyn"]}, {A["ferrara"]}, {A["fiszbein"]}, and {A["pearson"]}), funded by the [National Science Foundation](https://www.nsf.gov/awardsearch/show-award?AWD_ID=2446921) and the [Russell Sage Foundation](https://www.russellsage.org/research/grants/geography-race-and-ethnicity-united-states-uncovering-hidden-history-expulsion-and).',
 ':::','',
 '::: {.entry}',
 f'"The Economic Effects of the 1878 Yellow Fever Epidemic" (with {A["alster"]}, {A["bazzi"]}, and {A["zivin"]}).',
 ':::','']

open("/Users/patricktesta/website/research/index.qmd","w").write("\n".join(doc))
n_abs=sum(1 for p in WORKING+PUBS if ABS.get(p["slug"]))
print(f"wrote research/index.qmd: {len(WORKING)+len(PUBS)} entries, {n_abs} with abstracts, "
      f"{len(WORKING)+len(PUBS)} with BibTeX")
