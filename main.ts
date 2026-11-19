// Entry program for the make.fun bounty "gta6-meme-x-01" (Node 22, standard library only).
//
// The entry itself is a post on X: a GTA 6 meme whose picture carries make.fun's ghost
// mascot, posted publicly with @makefunai and the entrant's play code in its text.
// This program has exactly one job: copy POST.json from the repository root (the bot
// directory) to the output directory, where the house's gate reads it and then reads
// the post itself from X.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR stand in
// for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

// The grader runs this program twice and expects identical output bytes, so the
// copy is a plain byte-for-byte file copy with no timestamps or extra output.
mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
