# delphin-latex

LaTeX exporters for DELPH-IN data.

Currently only one exporter is available:

* `delphin.codecs.dmrstikz` -- export DMRS for rendering with
  [`tikz-dependency`][]

Contributions of other exporters are welcome!


# Example

Here is an image of the PDF produced for the DMRS for "The chef whose
soup spilled quit":

![DMRS rendering for "The chef whose soup spilled quit."](images/dmrs-tikz-pdf.png)


# Installation and Requirements

This package is a plugin for [PyDelphin][]. It is distributed with
PyDelphin by default, but otherwise it can be installed via `pip`:

``` console
$ pip install delphin-latex
```

It depends on the `delphin.dmrs` and `delphin.predicate` packages,
both at version `1.0.0`. For rendering, [LaTeX][] and the
[`tikz-dependency`] package are required.


# Related

For visually presenting MRSs, DMRSs, and derivation trees, you may
also be interested in [delphin-viz][] which can save visualizations as
PNG or SVG files.

[delphin-viz]: https://github.com/delph-in/delphin-viz
[LaTeX]: https://www.latex-project.org/
[PyDelphin]: https://github.com/delph-in/pydelphin/
[`tikz-dependency`]: https://ctan.org/pkg/tikz-dependency
