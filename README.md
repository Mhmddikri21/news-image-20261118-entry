# news-image-20261118

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Mhmddikri21/news-image-20261118-entry/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Mhmddikri21/news-image-20261118-entry/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for the make.fun bounty **"Sum up 18 November's world news in one image"** ($250, top 50 paid).

One broadsheet image — **Wednesday 18 November 2026, 55 stories, 7 regions** — drawn
entirely with Pillow (stdlib-free, no network, no randomness): a UTC timeline strip,
four lead cards (Kerch Bridge hit for a second day; Iran's retaliation after the US
Qeshm strike; Xi and Putin meeting in Shenzhen; Voyager 1 crossing one light-day),
a 12-card grid, a world map with numbered story dots, a 39-item also-list, and a
DATE CHECK box listing the stories deliberately left out because they broke before
Wednesday (the FAA ground stop on 13 Nov; Nvidia's board ruling out Huang's return
and its $115.8bn quarter, Peltola's Alaska win, the measles-status loss and the Quad
meeting in Manila, all 17 Nov; the Ebola tally passing 11,000). The Xi–Trump–Putin
trilateral is listed as due Thursday 19 Nov — not yet happened.

Every story was verified against 18 November 2026 reporting (Reuters, AFP, AP,
Al Jazeera, PAHO, WHO, NASA, UEFA, NBA). Anything one side merely claimed is
labelled CLAIM. The image is 1024×1024 and 196 KB, under the 1 MiB limit.

## Layout

- `main.py` — the entrypoint: copies `entry.png` to `/output/entry.png` and
  verifies the output is a valid 1024×1024 PNG. Run as `python3 main.py`
  (Python 3.13, stdlib only).
- `entry.png` — the rendered broadsheet (1024×1024).
- `.makefun/owner.json` — the entry wallet for the repo-owner check.

## How it was built

The image was composed from the previous day's winning template (the
news-image-20261117 final top 10, all at 45–50 stories with a UTC timeline
and a DATE CHECK box), with the story list researched from wire reporting
for 18 November and the design reviewed by a second model (GPT-6 Luna)
before the build. The builder asserts every text block fits its box, so
nothing overflows or clips.
