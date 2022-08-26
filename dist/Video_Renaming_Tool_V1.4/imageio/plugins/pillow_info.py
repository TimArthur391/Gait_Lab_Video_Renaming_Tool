# -*- coding: utf-8 -*-

# styletest: ignore E122 E123 E501

"""
Module that contain info about the Pillow formats. The first part of
this module generates this info and writes it to its own bottom half
if run as a script.
"""


def generate_info():  # pragma: no cover
    from urllib.request import urlopen
    import PIL
    from PIL import Image

    Image.init()

    ids = []
    formats = []
    docs = {}

    # Collect formats and their summary from plugin modules
    for mod_name in dir(PIL):
        if "ImagePlugin" in mod_name:
            mod = getattr(PIL, mod_name)
            for ob_name in dir(mod):
                ob = getattr(mod, ob_name)
                if isinstance(ob, type) and issubclass(ob, Image.Image):
                    if ob.format in ids:
                        print("Found duplicate for", ob.format)
                    else:
                        ids.append(ob.format)
                        formats.append((ob.format, ob.format_description))

    # Add extension info
    for i in range(len(formats)):
        id, summary = formats[i]
        ext = " ".join([e for e in Image.EXTENSION if Image.EXTENSION[e] == id])
        formats[i] = id, summary, ext

    # Get documentation of formats
    url = "https://raw.githubusercontent.com/python-pillow/Pillow/master/docs/handbook/image-file-formats.rst"  # noqa
    lines = urlopen(url).read().decode().splitlines()
    lines.append("End")
    lines.append("---")  # for the end

    # Parse documentation
    cur_name = ""
    cur_part = []
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith(("^^^", "---", "===")):
            if cur_name and cur_name in ids:
                text = "\n".join(cur_part[:-1])
                text = text.replace("versionadded::", "versionadded:: Pillow ")
                text = text.replace("Image.open`", "Image.write`")
                docs[cur_name] = text
            cur_part = []
            cur_name = lines[i - 1].strip().replace(" ", "").upper()
        else:
            cur_part.append("    " + line)

    # Fill in the blancs
    for id in ids:
        if id in docs:
            docs[id] = "*From the Pillow docs:*\n\n" + docs[id]
        else:
            docs[id] = "No docs for %s." % id
            print("no docs for", id)

    # Sort before writing
    formats.sort(key=lambda x: x[0])
    ids.sort()

    # Read file ...
    code = open(__file__, "rb").read().decode()
    code, divider, _ = code.partition("## BELOW IS " + "AUTOGENERATED")
    code += divider + "\n\n"

    # Write formats
    code += "pillow_formats = [\n"
    for i in range(len(formats)):
        print(formats[i])
        code += "    (%r, %r, %r),\n" % formats[i]
    code += "    ]\n\n\n"

    # Write docs
    code += "pillow_docs = {\n"
    for id in ids:
        code += '%r:\nu"""%s""",\n' % (id, docs[id])
    code += "}\n"

    # Write back
    with open(__file__, "wb") as f:
        f.write(code.encode())


if __name__ == "__main__":
    generate_info()


# BELOW IS AUTOGENERATED

pillow_formats = [
    ("BMP", "Windows Bitmap", ".bmp"),
    ("BUFR", "BUFR", ".bufr"),
    ("CUR", "Windows Cursor", ".cur"),
    ("DCX", "Intel DCX", ".dcx"),
    ("DDS", "DirectDraw Surface", ".dds"),
    ("DIB", "Windows Bitmap", ""),
    ("EPS", "Encapsulated Postscript", ".ps .eps"),
    ("FITS", "FITS", ".fit .fits"),
    ("FLI", "Autodesk FLI/FLC Animation", ".fli .flc"),
    ("FPX", "FlashPix", ".fpx"),
    ("FTEX", "Texture File Format (IW2:EOC)", ".ftc .ftu"),
    ("GBR", "GIMP brush file", ".gbr"),
    ("GIF", "Compuserve GIF", ".gif"),
    ("GRIB", "GRIB", ".grib"),
    ("HDF5", "HDF5", ".h5 .hdf"),
    ("ICNS", "Mac OS icns resource", ".icns"),
    ("ICO", "Windows Icon", ".ico"),
    ("IM", "IFUNC Image Memory", ".im"),
    ("IMT", "IM Tools", ""),
    ("IPTC", "IPTC/NAA", ".iim"),
    ("JPEG", "JPEG (ISO 10918)", ".jfif .jpe .jpg .jpeg"),
    ("JPEG2000", "JPEG 2000 (ISO 15444)", ".jp2 .j2k .jpc .jpf .jpx .j2c"),
    ("MCIDAS", "McIdas area file", ""),
    ("MIC", "Microsoft Image Composer", ".mic"),
    ("MPEG", "MPEG", ".mpg .mpeg"),
    ("MPO", "MPO (CIPA DC-007)", ".mpo"),
    ("MSP", "Windows Paint", ".msp"),
    ("PCD", "Kodak PhotoCD", ".pcd"),
    ("PCX", "Paintbrush", ".pcx"),
    ("PIXAR", "PIXAR raster image", ".pxr"),
    ("PNG", "Portable network graphics", ".png"),
    ("PPM", "Pbmplus image", ".pbm .pgm .ppm"),
    ("PSD", "Adobe Photoshop", ".psd"),
    ("SGI", "SGI Image File Format", ".bw .rgb .rgba .sgi"),
    ("SPIDER", "Spider 2D image", ""),
    ("SUN", "Sun Raster File", ".ras"),
    ("TGA", "Targa", ".tga"),
    ("TIFF", "Adobe TIFF", ".tif .tiff"),
    ("WMF", "Windows Metafile", ".wmf .emf"),
    ("XBM", "X11 Bitmap", ".xbm"),
    ("XPM", "X11 Pixel Map", ".xpm"),
    ("XVThumb", "XV thumbnail image", ""),
]


pillow_docs = {
    "BMP": u"""*From the Pillow docs:*


    PIL reads and writes Windows and OS/2 BMP files containing ``1``, ``L``, ``P``,
    or ``RGB`` data. 16-colour images are read as ``P`` images. Run-length encoding
    is not supported.

    The :py:meth:`~PIL.Image.Image.write` method sets the following
    :py:attr:`~PIL.Image.Image.info` properties:

    **compression**
        Set to ``bmp_rle`` if the file is run-length encoded.
    """,
    "BUFR": u"""*From the Pillow docs:*


    .. versionadded:: Pillow  1.1.3

    PIL provides a stub driver for BUFR files.

    To add read or write support to your application, use
    :py:func:`PIL.BufrStubImagePlugin.register_handler`.
    """,
    "CUR": u"""*From the Pillow docs:*


    CUR is used to store cursors on Windows. The CUR decoder reads the largest
    available cursor. Animated cursors are not supported.
    """,
    "DCX": u"""*From the Pillow docs:*


    DCX is a container file format for PCX files, defined by Intel. The DCX format
    is commonly used in fax applications. The DCX decoder can read files containing
    ``1``, ``L``, ``P``, or ``RGB`` data.

    When the file is opened, only the first image is read. You can use
    :py:meth:`~file.seek` or :py:mod:`~PIL.ImageSequence` to read other images.

    """,
    "DDS": u"""*From the Pillow docs:*


    DDS is a popular container texture format used in video games and natively
    supported by DirectX.
    Currently, DXT1, DXT3, and DXT5 pixel formats are supported and only in ``RGBA``
    mode.

    .. versionadded:: Pillow  3.4.0 DXT3
    """,
    "DIB": u"""No docs for DIB.""",
    "EPS": u"""*From the Pillow docs:*


    PIL identifies EPS files containing image data, and can read files that contain
    embedded raster images (ImageData descriptors). If Ghostscript is available,
    other EPS files can be read as well. The EPS driver can also write EPS
    images. The EPS driver can read EPS images in ``L``, ``LAB``, ``RGB`` and
    ``CMYK`` mode, but Ghostscript may convert the images to ``RGB`` mode rather
    than leaving them in the original color space. The EPS driver can write images
    in ``L``, ``RGB`` and ``CMYK`` modes.

    If Ghostscript is available, you can call the :py:meth:`~PIL.Image.Image.load`
    method with the following parameter to affect how Ghostscript renders the EPS

    **scale**
        Affects the scale of the resultant rasterized image. If the EPS suggests
        that the image be rendered at 100px x 100px, setting this parameter to
        2 will make the Ghostscript render a 200px x 200px image instead. The
        relative position of the bounding box is maintained::

            im = Image.open(...)
            im.size #(100,100)
            im.load(scale=2)
            im.size #(200,200)
    """,
    "FITS": u"""*From the Pillow docs:*


    .. versionadded:: Pillow  1.1.5

    PIL provides a stub driver for FITS files.

    To add read or write support to your application, use
    :py:func:`PIL.FitsStubImagePlugin.register_handler`.
    """,
    "FLI": u"""No docs for FLI.""",
    "FPX": u"""*From the Pillow docs:*


    PIL reads Kodak FlashPix files. In the current version, only the highest
    resolution image is read from the file, and the viewing transform is not taken
    into account.

    .. note::

        To enable full FlashPix support, you need to build and install the IJG JPEG
        library before building the Python Imaging Library. See the distribution
        README for details.
    """,
    "FTEX": u"""*From the Pillow docs:*


    .. versionadded:: Pillow  3.2.0

    The FTEX decoder reads textures used for 3D objects in
    Independence War 2: Edge Of Chaos. The plugin reads a single texture
    per file, in the compressed and uncompressed formats.
    """,
    "GBR": u"""*From the Pillow docs:*


    The GBR decoder reads GIMP brush files, version 1 and 2.

    The :py:meth:`~PIL.Image.Image.write` method sets the following
    :py:attr:`~PIL.Image.Image.info` properties:

    **comment**
        The brush name.

    **spacing**
        The spacing between the brushes, in pixels. Version 2 only.

    GD
    ^^

    PIL reads uncompressed GD files. Note that this file format cannot be
    automatically identified, so you must use :py:func:`PIL.GdImageFile.open` to
    read such a file.

    The :py:meth:`~PIL.Image.Image.write` method sets the following
    :py:attr:`~PIL.Image.Image.info` properties:

    **transparency**
        Transparency color index. This key is omitted if the image is not
        transparent.
    """,
    "GIF": u"""*From the Pillow docs:*


    PIL reads GIF87a and GIF89a versions of the GIF file format. The library writes
    run-length encoded files in GIF87a by default, unless GIF89a features
    are used or GIF89a is already in use.

    Note that GIF files are always read as grayscale (``L``)
    or palette mode (``P``) images.

    The :py:meth:`~PIL.Image.Image.write` method sets the following
    :py:attr:`~PIL.Image.Image.info` properties:

    **background**
        Default background color (a palette color index).

    **transparency**
        Transparency color index. This key is omitted if the image is not
        transparent.

    **version**
        Version (either ``GIF87a`` or ``GIF89a``).

    **duration**
        May not be present. The time to display the current frame
        of the GIF, in milliseconds.

    **loop**
        May not be present. The number of times the GIF should loop.

    Reading sequences
    ~~~~~~~~~~~~~~~~~

    The GIF loader supports the :py:meth:`~file.seek` and :py:meth:`~file.tell`
    methods. You can seek to the next frame (``im.seek(im.tell() + 1)``), or rewind
    the file by seeking to the first frame. Random access is not supported.

    ``im.seek()`` raises an ``EOFError`` if you try to seek after the last frame.

    Saving
    ~~~~~~

    When calling :py:meth:`~PIL.Image.Image.save`, the following options
    are available::

        im.save(out, save_all=True, append_images=[im1, im2, ...])

    **save_all**
        If present and true, all frames of the image will be saved. If
        not, then only the first frame of a multiframe image will be saved.

    **append_images**
        A list of images to append as additional frames. Each of the
        images in the list can be single or multiframe images.
        This is currently only supported for GIF, PDF, TIFF, and WebP.

    **duration**
        The display duration of each frame of the multiframe gif, in
        milliseconds. Pass a single integer for a constant duration, or a
        list or tuple to set the duration for each frame separately.

    **loop**
        Integer number of times the GIF should loop.

    **optimize**
        If present and true, attempt to compress the palette by
        eliminating unused colors. This is only useful if the palette can
        be compressed to the next smaller power of 2 elements.

    **palette**
        Use the specified palette for the saved image. The palette should
        be a bytes or bytearray object containing the palette entries in
        RGBRGB... form. It should be no more than 768 bytes. Alternately,
        the palette can be passed in as an
        :py:class:`PIL.ImagePalette.ImagePalette` object.

    **disposal**
        Indicates the way in which the graphic is to be treated after being displayed.

        * 0 - No disposal specified.
        * 1 - Do not dispose.
        * 2 - Restore to background color.
        * 3 - Restore to previous content.

         Pass a single integer for a constant disposal, or a list or tuple
         to set the disposal for each frame separately.

    Reading local images
    ~~~~~~~~~~~~~~~~~~~~

    The GIF loader creates an image memory the same size as the GIF file’s *logical
    screen size*, and pastes the actual pixel data (the *local image*) into this
    image. If you only want the actual pixel rectangle, you can manipulate the
    :py:attr:`~PIL.Image.Image.size` and :py:attr:`~PIL.Image.Image.tile`
    attributes before loading the file::

        im = Image.open(...)

        if im.tile[0][0] == "gif":
            # only read the first "local image" from this GIF file
            tag, (x0, y0, x1, y1), offset, extra = im.tile[0]
            im.size = (x1 - x0, y1 - y0)
            im.tile = [(tag, (0, 0) + im.size, offset, extra)]
    """,
    "GRIB": u"""*From the Pillow docs:*


    .. versionadded:: Pillow  1.1.5

    PIL provides a stub driver for GRIB files.

    The driver requires the file to start with a GRIB header. If you have files
    with embedded GRIB data, or files with multiple GRIB fields, your application
    has to seek to the header before passing the file handle to PIL.

    To add read or write support to your application, use
    :py:func:`PIL.GribStubImagePlugin.register_handler`.
    """,
    "HDF5": u"""*From the Pillow docs:*


    .. versionadded:: Pillow  1.1.5

    PIL provides a stub driver for HDF5 files.

    To add read or write support to your application, use
    :py:func:`PIL.Hdf5StubImagePlugin.register_handler`.
    """,
    "ICNS": u"""*From the Pillow docs:*


    PIL reads and (macOS only) writes macOS ``.icns`` files.  By default, the
    largest available icon is read, though you can override this by setting the
    :py:attr:`~PIL.Image.Image.size` property before calling
    :py:meth:`~PIL.Image.Image.load`.  The :py:meth:`~PIL.Image.Image.write` method
    sets the following :py:attr:`~PIL.Image.Image.info` property:

    **sizes**
        A list of supported sizes found in this icon file; these are a
        3-tuple, ``(width, height, scale)``, where ``scale`` is 2 for a retina
        icon and 1 for a standard icon.  You *are* permitted to use this 3-tuple
        format for the :py:attr:`~PIL.Image.Image.size` property if you set it
        before calling :py:meth:`~PIL.Image.Image.load`; after loading, the size
        will be reset to a 2-tuple containing pixel dimensions (so, e.g. if you
        ask for ``(512, 512, 2)``, the final value of
        :py:attr:`~PIL.Image.Image.size` will be ``(1024, 1024)``).
    """,
    "ICO": u"""*From the Pillow docs:*


    ICO is used to store icons on Windows. The largest available icon is read.

    The :py:meth:`~PIL.Image.Image.save` method supports the following options:

    **sizes**
        A list of sizes including in this ico file; these are a 2-tuple,
        ``(width, height)``; Default to ``[(16, 16), (24, 24), (32, 32), (48, 48),
        (64, 64), (128, 128), (256, 256)]``. Any sizes bigger than the original
        size or 256 will be ignored.

    IM
    ^^

    IM is a format used by LabEye and other applications based on the IFUNC image
    processing library. The library reads and writes most uncompressed interchange
    versions of this format.

    IM is the only format that can store all internal PIL formats.
    """,
    "IM": u"""No docs for IM.""",
    "IMT": u"""*From the Pillow docs:*


    PIL reads Image Tools images containing ``L`` data.
    """,
    "IPTC": u"""No docs for IPTC.""",
    "JPEG": u"""*From the Pillow docs:*


    PIL reads JPEG, JFIF, and Adobe JPEG files containing ``L``, ``RGB``, or
    ``CMYK`` data. It writes standard and progressive JFIF files.

    Using the :py:meth:`~PIL.Image.Image.draft` method, you can speed things up by
    converting ``RGB`` images to ``L``, and resize images to 1/2, 1/4 or 1/8 of
    their original size while loading them.

    The :py:meth:`~PIL.Image.Image.write` method may set the following
    :py:attr:`~PIL.Image.Image.info` properties if available:

    **jfif**
        JFIF application marker found. If the file is not a JFIF file, this key is
        not present.

    **jfif_version**
        A tuple representing the jfif version, (major version, minor version).

    **jfif_density**
        A tuple representing the pixel density of the image, in units specified
        by jfif_unit.

    **jfif_unit**
        Units for the jfif_density:

        * 0 - No Units
        * 1 - Pixels per Inch
        * 2 - Pixels per Centimeter

    **dpi**
        A tuple representing the reported pixel density in pixels per inch, if
        the file is a jfif file and the units are in inches.

    **adobe**
        Adobe application marker found. If the file is not an Adobe JPEG file, this
        key is not present.

    **adobe_transform**
        Vendor Specific Tag.

    **progression**
        Indicates that this is a progressive JPEG file.

    **icc_profile**
        The ICC color profile for the image.

    **exif**
        Raw EXIF data from the image.


    The :py:meth:`~PIL.Image.Image.save` method supports the following options:

    **quality**
        The image quality, on a scale from 1 (worst) to 95 (best). The default is
        75. Values above 95 should be avoided; 100 disables portions of the JPEG
        compression algorithm, and results in large files with hardly any gain in
        image quality.

    **optimize**
        If present and true, indicates that the encoder should make an extra pass
        over the image in order to select optimal encoder settings.

    **progressive**
        If present and true, indicates that this image should be stored as a
        progressive JPEG file.

    **dpi**
        A tuple of integers representing the pixel density, ``(x,y)``.

    **icc_profile**
        If present and true, the image is stored with the provided ICC profile.
        If this parameter is not provided, the image will be saved with no profile
        attached. To preserve the existing profile::

            im.save(filename, 'jpeg', icc_profile=im.info.get('icc_profile'))

    **exif**
        If present, the image will be stored with the provided raw EXIF data.

    **subsampling**
        If present, sets the subsampling for the encoder.

        * ``keep``: Only valid for JPEG files, will retain the original image setting.
        * ``4:4:4``, ``4:2:2``, ``4:2:0``: Specific sampling values
        * ``-1``: equivalent to ``keep``
        * ``0``: equivalent to ``4:4:4``
        * ``1``: equivalent to ``4:2:2``
        * ``2``: equivalent to ``4:2:0``

    **qtables**
        If present, sets the qtables for the encoder. This is listed as an
        advanced option for wizards in the JPEG documentation. Use with
        caution. ``qtables`` can be one of several types of values:

        *  a string, naming a preset, e.g. ``keep``, ``web_low``, or ``web_high``
        *  a list, tuple, or dictionary (with integer keys =
           range(len(keys))) of lists of 64 integers. There must be
           between 2 and 4 tables.

        .. versionadded:: Pillow  2.5.0


    .. note::

        To enable JPEG support, you need to build and install the IJG JPEG library
        before building the Python Imaging Library. See the distribution README for
        details.
    """,
    "JPEG2000": u"""*From the Pillow docs:*


    .. versionadded:: Pillow  2.4.0

    PIL reads and writes JPEG 2000 files containing ``L``, ``LA``, ``RGB`` or
    ``RGBA`` data.  It can also read files containing ``YCbCr`` data, which it
    converts on read into ``RGB`` or ``RGBA`` depending on whether or not there is
    an alpha channel.  PIL supports JPEG 2000 raw codestreams (``.j2k`` files), as
    well as boxed JPEG 2000 files (``.j2p`` or ``.jpx`` files).  PIL does *not*
    support files whose components have different sampling frequencies.

    When loading, if you set the ``mode`` on the image prior to the
    :py:meth:`~PIL.Image.Image.load` method being invoked, you can ask PIL to
    convert the image to either ``RGB`` or ``RGBA`` rather than choosing for
    itself.  It is also possible to set ``reduce`` to the number of resolutions to
    discard (each one reduces the size of the resulting image by a factor of 2),
    and ``layers`` to specify the number of quality layers to load.

    The :py:meth:`~PIL.Image.Image.save` method supports the following options:

    **offset**
        The image offset, as a tuple of integers, e.g. (16, 16)

    **tile_offset**
        The tile offset, again as a 2-tuple of integers.

    **tile_size**
        The tile size as a 2-tuple.  If not specified, or if set to None, the
        image will be saved without tiling.

    **quality_mode**
        Either `"rates"` or `"dB"` depending on the units you want to use to
        specify image quality.

    **quality_layers**
        A sequence of numbers, each of which represents either an approximate size
        reduction (if quality mode is `"rates"`) or a signal to noise ratio value
        in decibels.  If not specified, defaults to a single layer of full quality.

    **num_resolutions**
        The number of different image resolutions to be stored (which corresponds
        to the number of Discrete Wavelet Transform decompositions plus one).

    **codeblock_size**
        The code-block size as a 2-tuple.  Minimum size is 4 x 4, maximum is 1024 x
        1024, with the additional restriction that no code-block may have more
        than 4096 coefficients (i.e. the product of the two numbers must be no
        greater than 4096).

    **precinct_size**
        The precinct size as a 2-tuple.  Must be a power of two along both axes,
        and must be greater than the code-block size.

    **irreversible**
        If ``True``, use the lossy Irreversible Color Transformation
        followed by DWT 9-7.  Defaults to ``False``, which means to use the
        Reversible Color Transformation with DWT 5-3.

    **progression**
        Controls the progression order; must be one of ``"LRCP"``, ``"RLCP"``,
        ``"RPCL"``, ``"PCRL"``, ``"CPRL"``.  The letters stand for Component,
        Position, Resolution and Layer respectively and control the order of
        encoding, the idea being that e.g. an image encoded using LRCP mode can
        have its quality layers decoded as they arrive at the decoder, while one
        encoded using RLCP mode will have increasing resolutions decoded as they
        arrive, and so on.

    **cinema_mode**
        Set the encoder to produce output compliant with the digital cinema
        specifications.  The options here are ``"no"`` (the default),
        ``"cinema2k-24"`` for 24fps 2K, ``"cinema2k-48"`` for 48fps 2K, and
        ``"cinema4k-24"`` for 24fps 4K.  Note that for compliant 2K files,
        *at least one* of your image dimensions must match 2048 x 1080, while
        for compliant 4K files, *at least one* of the dimensions must match
        4096 x 2160.

    .. note::

       To enable JPEG 2000 support, you need to build and install the OpenJPEG
       library, version 2.0.0 or higher, before building the Python Imaging
       Library.

       Windows users can install the OpenJPEG binaries available on the
       OpenJPEG website, but must add them to their PATH in order to use PIL (if
       you fail to do this, you will get errors about not being able to load the
       ``_imaging`` DLL).
    """,
    "MCIDAS": u"""*From the Pillow docs:*


    PIL identifies and reads 8-bit McIdas area files.
    """,
    "MIC": u"""*From the Pillow docs:*


    PIL identifies and reads Microsoft Image Composer (MIC) files. When opened, the
    first sprite in the file is loaded. You can use :py:meth:`~file.seek` and
    :py:meth:`~file.tell` to read other sprites from the file.

    Note that there may be an embedded gamma of 2.2 in MIC files.
    """,
    "MPEG": u"""*From the Pillow docs:*


    PIL identifies MPEG files.
    """,
    "MPO": u"""*From the Pillow docs:*


    Pillow identifies and reads Multi Picture Object (MPO) files, loading the primary
    image when first opened. The :py:meth:`~file.seek` and :py:meth:`~file.tell`
    methods may be used to read other pictures from the file. The pictures are
    zero-indexed and random access is supported.
    """,
    "MSP": u"""*From the Pillow docs:*


    PIL identifies and reads MSP files from Windows 1 and 2. The library writes
    uncompressed (Windows 1) versions of this format.
    """,
    "PCD": u"""*From the Pillow docs:*


    PIL reads PhotoCD files containing ``RGB`` data. This only reads the 768x512
    resolution image from the file. Higher resolutions are encoded in a proprietary
    encoding.
    """,
    "PCX": u"""*From the Pillow docs:*


    PIL reads and writes PCX files containing ``1``, ``L``, ``P``, or ``RGB`` data.
    """,
    "PIXAR": u"""*From the Pillow docs:*


    PIL provides limited support for PIXAR raster files. The library can identify
    and read “dumped” RGB files.

    The format code is ``PIXAR``.
    """,
    "PNG": u"""*From the Pillow docs:*


    PIL identifies, reads, and writes PNG files containing ``1``, ``L``, ``P``,
    ``RGB``, or ``RGBA`` data. Interlaced files are supported as of v1.1.7.

    The :py:meth:`~PIL.Image.Image.write` method sets the following
    :py:attr:`~PIL.Image.Image.info` properties, when appropriate:

    **chromaticity**
        The chromaticity points, as an 8 tuple of floats. (``White Point
        X``, ``White Point Y``, ``Red X``, ``Red Y``, ``Green X``, ``Green
        Y``, ``Blue X``, ``Blue Y``)

    **gamma**
        Gamma, given as a floating point number.

    **srgb**
        The sRGB rendering intent as an integer.

          * 0 Perceptual
          * 1 Relative Colorimetric
          * 2 Saturation
          * 3 Absolute Colorimetric

    **transparency**
        For ``P`` images: Either the palette index for full transparent pixels,
        or a byte string with alpha values for each palette entry.

        For ``L`` and ``RGB`` images, the color that represents full transparent
        pixels in this image.

        This key is omitted if the image is not a transparent palette image.

    ``Open`` also sets ``Image.text`` to a list of the values of the
    ``tEXt``, ``zTXt``, and ``iTXt`` chunks of the PNG image. Individual
    compressed chunks are limited to a decompressed size of
    ``PngImagePlugin.MAX_TEXT_CHUNK``, by default 1MB, to prevent
    decompression bombs. Additionally, the total size of all of the text
    chunks is limited to ``PngImagePlugin.MAX_TEXT_MEMORY``, defaulting to
    64MB.

    The :py:meth:`~PIL.Image.Image.save` method supports the following options:

    **optimize**
        If present and true, instructs the PNG writer to make the output file as
        small as possible. This includes extra processing in order to find optimal
        encoder settings.

    **transparency**
        For ``P``, ``L``, and ``RGB`` images, this option controls what
        color image to mark as transparent.

        For ``P`` images, this can be a either the palette index,
        or a byte string with alpha values for each palette entry.

    **dpi**
        A tuple of two numbers corresponding to the desired dpi in each direction.

    **pnginfo**
        A :py:class:`PIL.PngImagePlugin.PngInfo` instance containing text tags.

    **compress_level**
        ZLIB compression level, a number between 0 and 9: 1 gives best speed,
        9 gives best compression, 0 gives no compression at all. Default is 6.
        When ``optimize`` option is True ``compress_level`` has no effect
        (it is set to 9 regardless of a value passed).

    **icc_profile**
        The ICC Profile to include in the saved file.

    **bits (experimental)**
        For ``P`` images, this option controls how many bits to store. If omitted,
        the PNG writer uses 8 bits (256 colors).

    **dictionary (experimental)**
        Set the ZLIB encoder dictionary.

    .. note::

        To enable PNG support, you need to build and install the ZLIB compression
        library before building the Python Imaging Library. See the installation
        documentation for details.
    """,
    "PPM": u"""*From the Pillow docs:*


    PIL reads and writes PBM, PGM and PPM files containing ``1``, ``L`` or ``RGB``
    data.
    """,
    "PSD": u"""*From the Pillow docs:*


    PIL identifies and reads PSD files written by Adobe Photoshop 2.5 and 3.0.

    """,
    "SGI": u"""*From the Pillow docs:*


    Pillow reads and writes uncompressed ``L``, ``RGB``, and ``RGBA`` files.

    """,
    "SPIDER": u"""*From the Pillow docs:*


    PIL reads and writes SPIDER image files of 32-bit floating point data
    ("F;32F").

    PIL also reads SPIDER stack files containing sequences of SPIDER images. The
    :py:meth:`~file.seek` and :py:meth:`~file.tell` methods are supported, and
    random access is allowed.

    The :py:meth:`~PIL.Image.Image.write` method sets the following attributes:

    **format**
        Set to ``SPIDER``

    **istack**
        Set to 1 if the file is an image stack, else 0.

    **nimages**
        Set to the number of images in the stack.

    A convenience method, :py:meth:`~PIL.Image.Image.convert2byte`, is provided for
    converting floating point data to byte data (mode ``L``)::

        im = Image.open('image001.spi').convert2byte()

    Writing files in SPIDER format
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The extension of SPIDER files may be any 3 alphanumeric characters. Therefore
    the output format must be specified explicitly::

        im.save('newimage.spi', format='SPIDER')

    For more information about the SPIDER image processing package, see the
    `SPIDER homepage`_ at `Wadsworth Center`_.

    .. _SPIDER homepage: https://spider.wadsworth.org/spider_doc/spider/docs/spider.html
    .. _Wadsworth Center: https://www.wadsworth.org/
    """,
    "SUN": u"""No docs for SUN.""",
    "TGA": u"""*From the Pillow docs:*


    PIL reads 24- and 32-bit uncompressed and run-length encoded TGA files.
    """,
    "TIFF": u"""*From the Pillow docs:*


    Pillow reads and writes TIFF files. It can read both striped and tiled
    images, pixel and plane interleaved multi-band images. If you have
    libtiff and its headers installed, PIL can read and write many kinds
    of compressed TIFF files. If not, PIL will only read and write
    uncompressed files.

    .. note::

        Beginning in version 5.0.0, Pillow requires libtiff to read or
        write compressed files. Prior to that release, Pillow had buggy
        support for reading Packbits, LZW and JPEG compressed TIFFs
        without using libtiff.

    The :py:meth:`~PIL.Image.Image.write` method sets the following
    :py:attr:`~PIL.Image.Image.info` properties:

    **compression**
        Compression mode.

        .. versionadded:: Pillow  2.0.0

    **dpi**
        Image resolution as an ``(xdpi, ydpi)`` tuple, where applicable. You can use
        the :py:attr:`~PIL.Image.Image.tag` attribute to get more detailed
        information about the image resolution.

        .. versionadded:: Pillow  1.1.5

    **resolution**
        Image resolution as an ``(xres, yres)`` tuple, where applicable. This is a
        measurement in whichever unit is specified by the file.

        .. versionadded:: Pillow  1.1.5


    The :py:attr:`~PIL.Image.Image.tag_v2` attribute contains a dictionary
    of TIFF metadata. The keys are numerical indexes from
    :py:attr:`~PIL.TiffTags.TAGS_V2`.  Values are strings or numbers for single
    items, multiple values are returned in a tuple of values. Rational
    numbers are returned as a :py:class:`~PIL.TiffImagePlugin.IFDRational`
    object.

        .. versionadded:: Pillow  3.0.0

    For compatibility with legacy code, the
    :py:attr:`~PIL.Image.Image.tag` attribute contains a dictionary of
    decoded TIFF fields as returned prior to version 3.0.0.  Values are
    returned as either strings or tuples of numeric values. Rational
    numbers are returned as a tuple of ``(numerator, denominator)``.

        .. deprecated:: 3.0.0


    Saving Tiff Images
    ~~~~~~~~~~~~~~~~~~

    The :py:meth:`~PIL.Image.Image.save` method can take the following keyword arguments:

    **save_all**
        If true, Pillow will save all frames of the image to a multiframe tiff document.

        .. versionadded:: Pillow  3.4.0

    **tiffinfo**
        A :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v2` object or dict
        object containing tiff tags and values. The TIFF field type is
        autodetected for Numeric and string values, any other types
        require using an :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v2`
        object and setting the type in
        :py:attr:`~PIL.TiffImagePlugin.ImageFileDirectory_v2.tagtype` with
        the appropriate numerical value from
        ``TiffTags.TYPES``.

        .. versionadded:: Pillow  2.3.0

        Metadata values that are of the rational type should be passed in
        using a :py:class:`~PIL.TiffImagePlugin.IFDRational` object.

        .. versionadded:: Pillow  3.1.0

        For compatibility with legacy code, a
        :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v1` object may
        be passed in this field. However, this is deprecated.

        .. versionadded:: Pillow  3.0.0

     .. note::

        Only some tags are currently supported when writing using
        libtiff. The supported list is found in
        :py:attr:`~PIL:TiffTags.LIBTIFF_CORE`.

    **compression**
        A string containing the desired compression method for the
        file. (valid only with libtiff installed) Valid compression
        methods are: ``None``, ``"tiff_ccitt"``, ``"group3"``,
        ``"group4"``, ``"tiff_jpeg"``, ``"tiff_adobe_deflate"``,
        ``"tiff_thunderscan"``, ``"tiff_deflate"``, ``"tiff_sgilog"``,
        ``"tiff_sgilog24"``, ``"tiff_raw_16"``

    These arguments to set the tiff header fields are an alternative to
    using the general tags available through tiffinfo.

    **description**

    **software**

    **date_time**

    **artist**

    **copyright**
        Strings

    **resolution_unit**
        A string of "inch", "centimeter" or "cm"

    **resolution**

    **x_resolution**

    **y_resolution**

    **dpi**
        Either a Float, 2 tuple of (numerator, denominator) or a
        :py:class:`~PIL.TiffImagePlugin.IFDRational`. Resolution implies
        an equal x and y resolution, dpi also implies a unit of inches.

    """,
    "WMF": u"""*From the Pillow docs:*


    PIL can identify playable WMF files.

    In PIL 1.1.4 and earlier, the WMF driver provides some limited rendering
    support, but not enough to be useful for any real application.

    In PIL 1.1.5 and later, the WMF driver is a stub driver. To add WMF read or
    write support to your application, use
    :py:func:`PIL.WmfImagePlugin.register_handler` to register a WMF handler.

    ::

        from PIL import Image
        from PIL import WmfImagePlugin

        class WmfHandler:
            def open(self, im):
                ...
            def load(self, im):
                ...
                return image
            def save(self, im, fp, filename):
                ...

        wmf_handler = WmfHandler()

        WmfImagePlugin.register_handler(wmf_handler)

        im = Image.open("sample.wmf")""",
    "XBM": u"""*From the Pillow docs:*


    PIL reads and writes X bitmap files (mode ``1``).
    """,
    "XPM": u"""*From the Pillow docs:*


    PIL reads X pixmap files (mode ``P``) with 256 colors or less.

    The :py:meth:`~PIL.Image.Image.write` method sets the following
    :py:attr:`~PIL.Image.Image.info` properties:

    **transparency**
        Transparency color index. This key is omitted if the image is not
        transparent.
    """,
    "XVThumb": u"""No docs for XVThumb.""",
}
