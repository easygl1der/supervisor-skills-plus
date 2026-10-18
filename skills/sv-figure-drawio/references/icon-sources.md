# Icon sources: order, registry, attribution

Icons in a paper figure come from real, licensed libraries. They are not
traced from the reference image and not invented when a library icon fits.
The sourcing order and the per-field registry are a user decision
[src: user:2026-10-13] (confirmed). The replica in the evidence project
already took a platform logo from a draw.io built-in stencil instead of
tracing it, and kept per-asset provenance
[src: arc:05-figures-tables/sources/drawio/overview-reference-replica/LAYOUT_FINGERPRINT.md; arc:05-figures-tables/sources/drawio/overview-reference-replica/SVG_ASSETS.md] (confirmed).

## Contents
1. Sourcing order
2. Registry (per field)
3. Licence notes that change how an icon may be used
4. Fetching and indexing a library
5. Attribution record
6. Adding a library to the registry
7. Gaps

## 1. Sourcing order

1. **draw.io built-in stencils.** Search the shape panel (or a draw.io MCP
   shape search, where available) for the concept first. Built-in stencils
   stay editable and need no embedded payload.
2. **Registered local libraries.** Libraries from section 2 that have been
   cloned locally and listed in `research.yaml` `figures.icon_libs` or env
   `ICON_LIBS`. Search them with `scripts/icon_index.py search`. Pick
   libraries tagged with the project's field (`research.yaml` `field`)
   first, then `general`.
3. **Web search** for an icon repository when nothing local fits. Open the
   repository, read its licence file and README licence section, clone it
   into `~/.cache/supervisor-skills/icons/<name>`, index it, and add a row
   to section 2 (section 6).
4. **Native shape.** Only then draw a simple native shape. Record it as
   `original` in the attribution file.

Within one figure, use one icon family (same stroke width, fill style and
corner radius) unless the reference mixes families on purpose.

## 2. Registry (per field)

Field tags: `se`, `ai-ml`, `math`, `stats`, `causal`, `bio`, `general`.
Kinds: `stencils`, `logos`, `concept icons`, `NN blocks`, `diagrams`
(complete figure sources to adapt), `scientific`.
Licence column: what the repository's licence file and README said when
read on the date given. Re-read it when fetching; licences change.

| # | Library | URL | Contains | Fields | Kinds | Licence as read (date) | How to fetch |
|---|---|---|---|---|---|---|---|
| 1 | draw.io built-in stencils | https://github.com/jgraph/drawio | Shape libraries shipped with draw.io (general, network, cloud, web logos, UML, BPMN and more) | general, se | stencils, logos | Code Apache-2.0 (LICENSE). README: icon sets and stencil libraries may not be used as assets in Atlassian products or marketplace apps without permission; end-user diagram output is exempt. Some icons come from third parties (2026-10-13) | Built into draw.io; search the shape panel. Stencil sources under `src/main/webapp/stencils` |
| 2 | draw.io community libraries | https://github.com/jgraph/drawio-libs | Custom libraries loadable by URL (`libs/`: carbon, fluent, phosphor, tabler, github, gitlab, health and others) | general, se | stencils, concept icons, logos | Repository Apache-2.0 (LICENSE). README marks per-library terms; at least one listed library states that no licence was given (2026-10-13) | Load a library by raw URL (File, Open Library from URL) or clone; check each library's own licence line in the README |
| 3 | NN-Models-drawio-library | https://github.com/HuanPP/NN-Models-drawio-library | 37 draw.io templates for neural-network architectures (CNN, transformer, other blocks) in IEEE-style pastel colours; `nn_model_library.xml`, `exports/drawio`, `exports/svg`, `exports/png` | ai-ml | NN blocks | MIT, copyright 2026 HuanPP (LICENSE) (2026-10-13) | `git clone --depth 1`; open `nn_model_library.xml` via File, Open Library |
| 4 | BioIcons | https://github.com/duerrsimon/bioicons | Life-science SVG icons; folders by licence (`static/icons/<licence>/<category>/<author>/`) with `icons.json`, `authors.json` | bio | scientific | Web app MIT (LICENSE). Icons carry individual licences (folders bsd, cc-0, cc-by-3.0, cc-by-4.0, cc-by-sa-3.0, cc-by-sa-4.0, mit); README: always cite each icon and its licence, state modifications for CC BY (2026-10-13) | `git clone --depth 1`; the index reads the licence folder per icon |
| 5 | Health Icons | https://github.com/resolvetosavelives/healthicons | Public-health and clinical icons, outline and filled, SVG and PNG; `public/icons/meta-data.json` | bio | scientific, concept icons | README: icons public domain (CC0); repository code MIT (LICENSE) (2026-10-13) | `git clone --depth 1`; index reads `meta-data.json` |
| 6 | Simple Icons | https://github.com/simple-icons/simple-icons | SVG brand logos for software, platforms and services (`icons/`, data in `data/`) | se, general | logos | Project CC0-1.0 (LICENSE.md). DISCLAIMER.md: not every icon is CC0; check per-icon licence data; brand marks remain trademarks (2026-10-13) | `git clone --depth 1`; check the icon's entry in the data file before use |
| 7 | SVG Logos (gilbarbara) | https://github.com/gilbarbara/logos | SVG logos of software tools, languages and services (`logos/`) | se | logos | CC0-1.0 (LICENSE.txt) (2026-10-13) | `git clone --depth 1` |
| 8 | Devicon | https://github.com/devicons/devicon | Icons for programming languages, design and development tools (`icons/<tool>/`) | se | logos | MIT, copyright 2015 konpa (LICENSE) (2026-10-13) | `git clone --depth 1` |
| 9 | Tabler Icons | https://github.com/tabler/tabler-icons | Over 6,200 SVG concept icons, outline and filled (`icons/outline`, `icons/filled`) | general, se, stats | concept icons | MIT, copyright Pawel Kuna (LICENSE) (2026-10-13) | `git clone --depth 1` |
| 10 | Lucide | https://github.com/lucide-icons/lucide | Concept icons, fork of Feather (`icons/`) | general, se | concept icons | ISC (LICENSE); icons derived from Feather listed in the same file are MIT, copyright Cole Bemis (2026-10-13) | `git clone --depth 1` |
| 11 | Material Design Icons / Symbols | https://github.com/google/material-design-icons | Google Material icons and symbols (`src/`, `symbols/`, `png/`) | general | concept icons | Apache-2.0 (LICENSE) (2026-10-13) | `git clone --depth 1` (large); or take single SVGs from `symbols/web` |
| 12 | Phosphor Icons | https://github.com/phosphor-icons/core | Concept icons in six weights (`assets/thin` to `assets/duotone`) | general | concept icons | MIT, copyright 2023 Phosphor Icons (LICENSE) (2026-10-13) | `git clone --depth 1` |
| 13 | Carbon icons and pictograms (IBM) | https://github.com/carbon-design-system/carbon | Monorepo; `packages/icons` (UI and concept icons) and `packages/pictograms` (larger concept illustrations) | general, se | concept icons | Apache-2.0 (LICENSE) (2026-10-13) | `git clone --depth 1 --filter=blob:none --sparse`, then sparse-checkout `packages/icons` |
| 14 | Font Awesome Free | https://github.com/FortAwesome/Font-Awesome | Icons as SVG (`svgs/solid`, `svgs/regular`, `svgs/brands`) and fonts | general, se | concept icons, logos | LICENSE.txt: icons as SVG and JS CC BY 4.0 (attribution required); font files SIL OFL 1.1 (2026-10-13) | `git clone --depth 1`; record attribution for every icon |
| 15 | ML Visuals (dair.ai) | https://github.com/dair-ai/ml-visuals | Over 100 editable ML figures and basic elements maintained in Google Slides | ai-ml | NN blocks, diagrams | Repository MIT, copyright 2020 dair.ai (LICENSE). README: free to reuse; credit to the designer named in the slide notes is requested (2026-10-13) | Open the slides linked in the README; File, Download; record the slide author |
| 16 | PlotNeuralNet | https://github.com/HarisIqbal88/PlotNeuralNet | LaTeX (TikZ) code and Python helpers for NN architecture diagrams (`layers/`, `pycore/`, `examples/`) | ai-ml | NN blocks, diagrams | MIT, copyright 2018 HarisIqbal88 (LICENSE) (2026-10-13) | `git clone --depth 1`; render with LaTeX |
| 17 | NN-SVG | https://github.com/alexlenail/NN-SVG | Generator for publication-ready NN architecture schematics (FCNN, LeNet and AlexNet styles) exported as SVG | ai-ml | NN blocks | MIT, copyright 2018 Alexander Lenail (LICENSE) (2026-10-13) | Run the web page from the repo or its hosted copy; export SVG |
| 18 | Scientific Diagrams (janosh) | https://github.com/janosh/diagrams | TikZ and Typst (CeTZ) sources of diagrams of physics, chemistry and machine-learning concepts (`assets/<diagram>/`), for example autoencoders, convolutions, distributions | ai-ml, math, stats | diagrams | MIT, copyright 2021 Janosh Riebesell (LICENSE) (2026-10-13) | `git clone --depth 1`; adapt the `.tex` or `.typ` source |
| 19 | PGF/TikZ figures (Velickovic) | https://github.com/PetarV-/TikZ | One folder per TikZ figure: neural-network layers (convolution, LSTM, GAN, attention on graphs), graph algorithms, HMMs, some computing and signal diagrams | ai-ml, math | diagrams | MIT, copyright 2016 Petar Velickovic (LICENSE) (2026-10-13) | `git clone --depth 1`; adapt the `.tex` source |
| 20 | tikz-bayesnet | https://github.com/jluttine/tikz-bayesnet | TikZ library for Bayesian networks, graphical models, plates and directed factor graphs | stats, causal, ai-ml | diagrams | MIT, copyright 2010-2011 Laura Dietz, 2012 Jaakko Luttinen (LICENSE; README says MIT) (2026-10-13) | `git clone --depth 1`; `\usetikzlibrary{bayesnet}` |

Fields with thin coverage: `causal` (row 20 only; draw causal DAGs as native
nodes and arrows or with tikz-bayesnet), `math` (TikZ collections only;
geometry and proof diagrams are normally drawn natively, see
`sv-figure-design` render-and-inspect loop), `stats` (plots come from the
analysis scripts, not icon libraries).

## 3. Licence notes that change how an icon may be used

- **CC0, MIT, ISC, Apache-2.0, BSD:** usable in a paper figure; record the
  row anyway. Apache-2.0 and MIT ask that the notice travel with copies of
  the software; for a figure, the attribution file is the record.
- **CC BY (Font Awesome icons, many BioIcons):** attribution is required.
  Put it in the attribution file and, where the venue allows, in the
  caption or acknowledgements. State modifications (recolour, crop).
- **CC BY-SA:** derivatives must carry the same licence; avoid in a figure
  unless the team accepts that.
- **Logos and brand marks:** a permissive repository licence does not grant
  trademark rights. Use a logo only to name the tool or platform it stands
  for, unmodified apart from colour where the brand guidelines allow.
- **draw.io stencils:** see row 1; the Atlassian restriction does not
  affect exported diagram images.
- **No licence found:** do not use. Record the library as `unknown` and
  pick another.

## 4. Fetching and indexing a library

```bash
mkdir -p ~/.cache/supervisor-skills/icons
git clone --depth 1 <url> ~/.cache/supervisor-skills/icons/<name>
# read LICENSE and the README licence section now; note the date
```

Register it in `research.yaml` (paths may use `~` and environment
variables; no machine-specific home paths in shared files):

```yaml
figures:
  icon_libs:
    - {name: tabler, path: ~/.cache/supervisor-skills/icons/tabler-icons,
       license: MIT, source: https://github.com/tabler/tabler-icons, retrieved: 2026-10-13}
    - {name: bioicons, path: ~/.cache/supervisor-skills/icons/bioicons,
       source: https://github.com/duerrsimon/bioicons, retrieved: 2026-10-13}
```

Or set `ICON_LIBS=path1:path2` for a one-off session. Then:

```bash
python "$SKILL_DIR/scripts/icon_index.py" build             # reads research.yaml and ICON_LIBS
python "$SKILL_DIR/scripts/icon_index.py" search "database" --license cc0,mit,apache,isc
python "$SKILL_DIR/scripts/icon_index.py" attribute --figure-dir figures/overview_icons \
    --id "tabler:icons/outline/database.svg"
```

The index is written to `~/.cache/supervisor-skills/icons/index.json` unless
`--out` is given. It understands BioIcons licence folders, Health Icons
metadata and draw.io `<mxlibrary>` files (each entry becomes one asset); any
other folder is indexed by file name and path. `attribute` refuses assets
whose licence is `unknown`.

## 5. Attribution record

Every icon used in a figure gets one row in `<figure>_icons/ATTRIBUTION.tsv`
next to the figure source, for example `figures/overview_icons/`.

| Column | Content |
|---|---|
| source | repository URL (or `draw.io built-in`, or `original`) |
| path | path inside the repository, or the stencil name (`mxgraph.<lib>.<shape>`) |
| license | licence as read from the repository at fetch time |
| author | icon author where the source names one (required for CC BY) |
| retrieved | date the library was fetched or the licence was read |
| asset_id | id from the index (empty for stencils and originals) |
| library | registry name |
| note | modifications: recoloured, cropped, simplified |

Original icons drawn for the figure get rows with source `original`, the
same way the evidence project's `SVG_ASSETS.md` marked each asset as
original, generic or derived.

## 6. Adding a library to the registry

1. Open the repository page; read the licence file and any README licence
   or disclaimer section. Do not add from memory.
2. Add a row: name, URL, what it contains (folders), field tags, kinds,
   licence as read with the date, how to fetch.
3. If icons carry individual licences, say so in the licence column.
4. Keep the registry to libraries useful for research figures; a library
   used once for one project belongs in that project's `research.yaml` only.

## 7. Gaps

- No library in the registry targets empirical software engineering
  concepts (issue, commit, review, CI run) as a coherent family; concept
  sets (rows 9 to 13) cover them with generic metaphors.
- Statistics and causal-inference icon sets with verified licences were not
  found; draw these diagrams natively.
