import os
import re
from pathlib import Path


def main() -> None:
    rendezvous = os.environ.get("CUSTOM_RENDEZVOUS_SERVER", "192.168.30.217")
    pub_key = os.environ.get(
        "CUSTOM_RS_PUB_KEY",
        "O2zV5EUeKHJFeousICtF3F+51T5UKSAbnsjCUVND1kk=",
    )
    path = Path("libs/hbb_common/src/config.rs")
    source = path.read_text()

    source = re.sub(
        r'pub const RENDEZVOUS_SERVERS: &\[&str\] = &\[[^\]]+\];',
        f'pub const RENDEZVOUS_SERVERS: &[&str] = &["{rendezvous}"];',
        source,
    )
    source = re.sub(
        r'pub const RS_PUB_KEY: &str = "[^"]+";',
        f'pub const RS_PUB_KEY: &str = "{pub_key}";',
        source,
    )

    path.write_text(source)
    print(f"Patched {path} with custom RustDesk server defaults.")


if __name__ == "__main__":
    main()
