# Custom RustDesk Build

This fork is preconfigured for the local self-hosted RustDesk server.

## Why this uses a patch script

`libs/hbb_common` is a git submodule.

If you edit `libs/hbb_common/src/config.rs` directly, your fork of `rustdesk/rustdesk`
will not permanently carry the file content unless you also fork and update the
`rustdesk/hbb_common` submodule pointer.

To avoid that maintenance burden, this fork patches the submodule during CI.

Patch script:

- `scripts/patch_custom_server.py`

Current values injected by the workflow:

- `CUSTOM_RENDEZVOUS_SERVER = "192.168.30.217"`
- `CUSTOM_RS_PUB_KEY = "O2zV5EUeKHJFeousICtF3F+51T5UKSAbnsjCUVND1kk="`

## GitHub Actions workflow

Manual build workflow:

- `.github/workflows/custom-macos-aarch64.yml`

It builds an unsigned macOS arm64 DMG and uploads it as an artifact named:

- `rustdesk-custom-macos-aarch64`

## How to use

1. Push this fork to GitHub.
2. Open `Actions`.
3. Run `Custom macOS aarch64 Build`.
4. Download the artifact DMG from the workflow run.

## If the server changes later

Update these two env values in `.github/workflows/custom-macos-aarch64.yml`:

- `CUSTOM_RENDEZVOUS_SERVER`
- `CUSTOM_RS_PUB_KEY`
