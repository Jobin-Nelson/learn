use clap::Parser;

#[derive(Debug, Parser)]
#[clap(author, version, about)]
pub struct LeetDailyArgs {
    /// create a file if not existing
    #[clap(short, long, action)]
    pub file: bool,

    /// open file in neovim
    #[clap(short, long, action)]
    pub vim: bool,
}
