Threatspec is an open source project that aims to close the gap between development and security by bringing the threat modelling process further into the development process. This is achieved by having developers and security engineers write threat specifications alongside code, then dynamically generating reports and data-flow diagrams from the code. This allows engineers to capture the security context of the code they write, as they write it.

Usage:

    # Install graphviz
    $ pip install threatspec
    $ cd path/to/code/repo
    $ threatspec init
    $ $EDITOR threatspec.yaml
    $ threatspec run
    $ threatspec report

You can now view and share the therat model report markdown file ThreatModel.md and the associated image ThreatModel.gv.png.

For more information see: https://github.com/threatspec/threatspec