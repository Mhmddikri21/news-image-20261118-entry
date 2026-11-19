# news-image-20261118

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Mhmddikri21/news-image-20261118-entry/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Mhmddikri21/news-image-20261118-entry/reward.svg)](https://make.fun/bounty/news-image-20261118)

An entry for the make.fun bounty **"Sum up 18 November's world news in one image"**
($250, top 50 paid).

The deliverable is a single broadsheet picture of **Wednesday 18 November 2026 —
55 stories across 7 regions** — drawn entirely with Pillow, no network and no
randomness. It opens with a UTC timeline strip, then four lead cards (the Kerch
Bridge struck for a second day; Iran's retaliation after the US strike on Qeshm;
Xi and Putin meeting in Shenzhen; Voyager 1 crossing one light-day), followed by
a 12-card grid, a world map with numbered story dots, a 39-item also-list, and a
DATE CHECK box for the stories deliberately left out because they broke before
Wednesday: the FAA ground stop of 13 Nov; Nvidia's board ruling out Huang's
return and its $115.8bn quarter, Peltola's Alaska win, the measles-status loss
and the Quad meeting in Manila (all 17 Nov); the Ebola tally passing 11,000.
The Xi–Trump–Putin trilateral is shown as due Thursday 19 Nov, not yet held.

Each story was checked against 18 November 2026 wire reporting (Reuters, AFP,
AP, Al Jazeera, PAHO, WHO, NASA, UEFA, NBA). Anything only one side claimed is
labelled CLAIM. The picture is 1024×1024 and 196 KB, inside the 1 MiB limit.

## Layout

- `main.py` — the entrypoint: copies `entry.png` to `/output/entry.png` and
  confirms the result is a valid 1024×1024 PNG. Run it as `python3 main.py`
  (Python 3.13, standard library only).
- `entry.png` — the finished broadsheet (1024×1024).
- `.makefun/owner.json` — the entry wallet used for the repo-owner check.

## How it was built

The layout follows the previous day's winning template (the news-image-20261117
final top 10, all at 45–50 stories with a UTC timeline and a DATE CHECK box).
The story list came from wire reporting for 18 November, and a second model
(GPT-6 Luna) reviewed the design before the build. The builder asserts that
every text block fits its box, so nothing overflows or clips.
