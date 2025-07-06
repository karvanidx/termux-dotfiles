# Fixing Syntax Highlighting in Helix

If you've configured a theme in Helix but still don't see any syntax highlighting, the problem is almost always that Helix cannot find the necessary Tree-sitter grammar files. Themes apply color, but grammars are what identify the code structures (keywords, functions, etc.) to be colored.

This tutorial will guide you through the simple steps to diagnose and fix this issue.

## Step 1: Diagnose the Issue with `hx --health`

The first step is to use Helix's built-in health check to confirm the problem.

Run the following command in your terminal:

```bash
hx --health
```

Look for the `Tree-sitter` section in the output. You will likely see `✘` marks next to the languages under the "Highlight" column, indicating that the highlighting grammar is not found. You may also see a message like `Runtime directory does not exist`.

## Step 2: Install Prerequisites

To fetch and build the grammars, you need `git` and a C/C++ compiler. If you don't have them, you can install them using your system's package manager.

For Debian-based systems (like Termux on Android), you can run:

```bash
pkg install build-essential git
```

## Step 3: Fetch the Grammars

Next, you need to download the source code for the grammars. Helix has a built-in command for this.

```bash
hx --grammar fetch
```

This command will download the grammar source files into Helix's runtime directory (usually `~/.config/helix/runtime`).

## Step 4: Build the Grammars

Once the source files are downloaded, you need to compile them into the shared library files (`.so`) that Helix uses.

```bash
hx --grammar build
```

This command will compile all the grammars that were just fetched.

## Step 5: Restart Helix

Finally, close and restart Helix to load the newly built grammars.

Your syntax highlighting should now be working perfectly.
