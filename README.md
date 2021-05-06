# Corpus of latrinalia

**WARNING:** Tsakorpus 2.0 is being developed right now. It is going to be released in May 2021.

If you want to use tsakorpus, download the most recent version from this repository.

## Tsakorpus

This corpus uses a linguistic corpus search platform called *tsakorpus*. This is a fork of the [tsakorpus repository](https://bitbucket.org/tsakorpus/tsakorpus/src/master/), which contains corpus-specific settings and the source data alongside the generic platform files. For information about installing and using tsakorpus, please refer to the tsakorpus repository.

Tsakorpus supports corpora with morphological annotation, special gloss search, multi-word search, subcorpus selection, automatic transliteration, word distribution charts, parallel corpora, and media-aligned corpora. Multiple interface languages are supported with Flask-Babel.

## Documentation

All documentation is available [here](https://tsakorpus.readthedocs.io/en/latest/). If you are not sure if Tsakorpus is what you need, read the [FAQ](https://tsakorpus.readthedocs.io/en/latest/faq.html). If you want to set up a corpus, start [here](https://tsakorpus.readthedocs.io/en/latest/overview.html).

Feel free to ask questions or discuss Tsakorpus [on the Discussions page](https://github.com/timarkh/tsakorpus/discussions/) or post [issues](https://github.com/timarkh/tsakorpus/issues).

The source files (images, metadata and transcriptions) are located in ``src_convertors/corpus``. You may use them as you wish; however, we would appreciate mentioning the authors and including the link either to this repository or to the web site.

Tsakorpus was tested on Windows and Ubuntu. Its dependencies are the following:

* elasticsearch 7.x (tested on 7.6, 7.7, 7.10, 7.12)
* python >= 3.5
* python modules: elasticsearch 7.x, flask, lxml, ijson, Flask-Babel, xlsxwriter (you can use requirements.txt)
* for converting media-aligned corpora: ffmpeg
* it is recommended to deploy tsakorpus through apache2 with wsgi or nginx

The following resources are used by tsakorpus, but do not need to be installed:

* [jQuery](https://jquery.com/) library
* [jQuery-Autocomplete](https://github.com/devbridge/jQuery-Autocomplete)
* [video.js](http://videojs.com/) media player
* [videojs-youtube](https://github.com/videojs/videojs-youtube) plugin
* [bootstrap](http://getbootstrap.com/) toolkit
* [D3.js](https://d3js.org/) visualization library
* [KioskBoard](https://github.com/furcan/KioskBoard) virtual keyboard

## License

The software is distributed under MIT license (see LICENSE).
