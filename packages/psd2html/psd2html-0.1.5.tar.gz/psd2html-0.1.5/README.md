PSD2HTML
=======

PSD to HTML converter based on `psd-tools`_.

.. _`psd-tools`: https://github.com/psd-tools/psd-tools

Usage
-----

The package comes with a command-line tool::

    psd2html input.psd output.html

When the output path is a directory, or omitted, the tool infers the output
name from the input::

    psd2html input.psd output/  # => output/input.html
    psd2html input.html          # => input.html

