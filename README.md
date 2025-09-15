# TERMUX-DOTFILES

My termux size keeps increases every day, someday I might wipe the data to save my 128GB of storage #lol

## Packages

The list of packages that I need to install separate by level:

### Important

```bash
# [1] Update, upgrade, and install needed packages \
pkg update && pkg upgrade -y && pkg in nala && \
    nala install automake \
    bat \
    binutils-is-llvm \
    brotli \
    build-essential \
    cmake \
    deno \
    golang \
    libopenblas libandroid-execinfo \
    nala \
    ncdu \
    neovim \
    ninja \
    net-tools \
    nodejs \
    nushell \
    openssh openssl \
    patchelf \ 
    python uv \
    wget \
    zellij -y \
    && \
# [2] Creating ~/.local/bin, then copy .local/ to ~/.local \
mkdir -p ~/.local/bin ~/.gemini ~/.termux && \
cp -r .local/ ~/.local && cp -r .termux ~/.termux && termux-reload-settings && touch ~/.hushlogin
```

### Additional

Sometimes to avoid bored times using Termux is playing with Alpine Linux through `proot-distro`.

```
pkg in proot-distro && proot-distro install alpine
```

The reasons I chooses Alpine is to get latest package version from the testing repo.
