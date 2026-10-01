---
title: ImageJAI
description: Conversational image analysis in Fiji with an embedded assistant, standalone console, cloud or local model selection, direct Fiji tools and reusable session macros.
categories: [Analysis, Automation]
source-url: https://github.com/Jay2owe/ImageJAI
update-site: ImageJ-AI
release-version: 0.5.0
release-date: 2026-09-29
dev-status: Active
support-status: Active
team-maintainers: '@Jay2owe'
license-url: https://github.com/Jay2owe/ImageJAI/blob/main/LICENSE
license-label: BSD-3-Clause
---

ImageJAI is an ImageJ/Fiji plugin for describing image analysis in plain
language. It offers an assistant inside Fiji and a standalone terminal
console. The agent can inspect open images, run macros, read measurements,
interact with plugin dialogs and check the result while the user supervises.

Users can choose a cloud model, a supported agent subscription or a local
model through Ollama. Model access is configured separately from the plugin.

## Installation

1. Start Fiji and choose {% include bc path="Help|Update..." %}.
2. Click **Manage update sites**.
3. Enable **ImageJAI** if listed. Otherwise add an unlisted site with the name
   `ImageJ-AI` and URL `https://sites.imagej.net/ImageJ-AI/`.
4. Apply changes and restart Fiji.
5. Open {% include bc path="Plugins|AI Assistant" %}.

Fiji must run Java 11 or newer. The embedded assistant runs from the plugin
JAR. The optional console requires internet access for its first setup.

## Standalone console setup

In the assistant, open **Settings > Models & Agents**, find **ImageJAI Console**
and click **Install**. The plugin creates a private Python environment and
installs the console's packages. If suitable Python is unavailable, it
downloads a private Python runtime; a manual Python installation is not
required. Setup does not require administrator access.

Launch the console from the same settings row, or run `imagejai` in a terminal.
Choose a model and sign in to its supported provider or connect to a local
model server. Provider subscriptions and usage charges are separate from
ImageJAI.

## Working with Fiji

For example, ask the assistant to open the sample Blobs image, blur it,
segment objects, measure fluorescence or export the results. ImageJAI uses
Fiji's available commands and can inspect unfamiliar plugin dialogs before
running them. It operates on open Fiji images, results tables and regions
of interest; supported file formats depend on the installed Fiji plugins.

The console detects or uses a saved Fiji installation. It can launch Fiji
and start ImageJAI's local TCP server automatically. Use `/fiji` to select
another installation and `/settings` to configure startup.

| Console control | Purpose |
| --- | --- |
| `/model` | Choose a model and its available reasoning effort levels |
| `/settings` | Configure the agent, Fiji, privacy, display and budget |
| **Session Macros** | Browse and reuse the current session's macros |
| `/help` | Show commands and keyboard controls |

Replies and activity are streamed into the conversation. Tool results have
short summaries with expandable details, and side panels can collapse to
give the chat more space. Saved sessions can be resumed later.

## Outputs and records

Analyses can create Fiji images, measurements and results tables. Exported
analysis files are written under `AI_Exports/` next to the source image.
The console records session macros and conversation history, allowing the
user to review or reuse the work.

## Privacy controls

New folders use **Standard** posture, which permits original filenames and
metadata in agent responses. Users can select **Pseudonymised** to filter
supported identifiers or **On-premises** to restrict supported launch routes
to local models. Saved folder choices are retained.

These controls cover ImageJAI's supported routes and responses. They do not
anonymise source images or govern tools outside ImageJAI. See the
[privacy guide](https://github.com/Jay2owe/ImageJAI/blob/main/docs/data-governance/README.md)
for the scope and limits.

## Scripting and external agents

ImageJAI exposes authenticated JSON commands through a local TCP server,
normally on port 7746. The public command documentation covers macro and
script execution, image inspection, results, dialogs and event subscriptions.
See the [command reference](https://github.com/Jay2owe/ImageJAI/blob/main/docs/COMMAND_API.md)
and [console guide](https://github.com/Jay2owe/ImageJAI/blob/main/docs/console/README.md).
