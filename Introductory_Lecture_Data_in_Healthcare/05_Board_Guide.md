# English freeform lecture map

Open `Data_in_Healthcare.excalidraw` in Excalidraw. All board text is English; delivery can remain Arabic.

Pan and zoom through an open map with circular clusters, curved connectors, hand-drawn strokes, and handwritten text. There are no slide frames. Small topic numbers help navigation.

Teaching route: **1 → 2 → 3 → 4 → 4B → 5 → 6 → 7 → 8 → 9**. Answer branch 4B is far to the right, away from the initial activity. The four analytics types surround the central “Reduce uncertainty” circle. Keep the 75-minute timing in the speaking notes.

## Current files

- `Data_in_Healthcare.excalidraw`: editable English map.
- `Freeform_Previews/Overview.png`: whole-map preview.
- `Freeform_Previews/Four_Types.png`: central concept close-up.
- `Freeform_Previews/Map.svg`: vector preview.
- `build_freeform_board.py`: current generator. Rerunning overwrites the board; preserve manual changes first.
- `render_freeform.cjs`: renders previews using locally installed dependencies.

The earlier Arabic board is preserved in `Archive/Data_in_Healthcare_framed_arabic.excalidraw`. The old `Board_Previews/`, `build_board.py`, and `render_board.cjs` belong to that earlier version; do not use them to regenerate the current board.

## Verification

Checked that all board text is English and there are no frame elements. Rendered and visually inspected the map and central concept, adjusting a connector to avoid an annotation. SVG previews use Comic Sans MS as a handwriting approximation. Native Excalidraw uses its handwritten font and rough strokes, so rendering can differ slightly. These are not native Excalidraw exports.

The user's default Excalidraw preferences are saved in the root `AGENTS.md` for future work in this repository.
