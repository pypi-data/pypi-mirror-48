pylresolv - DNS querying through libc libresolv.so using ctypes
===============================================================

Provides access to ``res_query`` (``resolver(3)``) and friends for very
basic DNS querying (beyond ``gethostbyname``).

*Right now, it only supports MX record lookups.*

This is *not* a replacement for fully featured DNS libraries like
``dnspython`` or ``pycares``, but rather a small wrapper to provide a bare
minimal lookup capability. Additionally, it serves as an example of how
to use ``-lresolv`` routines.

.. warning:: BEWARE!

    This library uses (a) not-so-well documented C library calls which
    (b) may differ in their ABI across different libc versions and
    operating systems. Proceed with caution. The only thing this has
    going for it, is its small size.


Most common usage
-----------------

.. code-block:: python

    from pylresolv import ns_parse, ns_type, res_query

    answer = res_query('gmail.com', rr_type=ns_type.ns_t_mx)
    ret = ns_parse(answer, handler=ns_type.handle_t_mx)
    print(ret)

Will produce a list of ``RR`` objects::

    [RR<ns_type.ns_t_mx: 15>((40, u'alt4.gmail-smtp-in.l.google.com')),
     RR<ns_type.ns_t_mx: 15>((30, u'alt3.gmail-smtp-in.l.google.com')),
     RR<ns_type.ns_t_mx: 15>((10, u'alt1.gmail-smtp-in.l.google.com')),
     RR<ns_type.ns_t_mx: 15>((20, u'alt2.gmail-smtp-in.l.google.com')),
     RR<ns_type.ns_t_mx: 15>((5, u'gmail-smtp-in.l.google.com'))]

Example from main:

.. code-block:: python

    from pprint import pprint
    queries = (
        ('gmail.com', ns_type.ns_t_ns),
        ('gmail.com', ns_type.ns_t_a),
        ('gmail.com', ns_type.ns_t_mx),
        ('gmail.com', ns_type.ns_t_txt),
        ('www.gmail.com', ns_type.ns_t_cname),
    )
    for qhost, qtype in queries:
        print('Querying host {!r} type {!r}:'.format(qhost, qtype))
        answer = res_query(qhost, rr_type=qtype)
        ret = ns_parse(answer)
        # ret = ns_parse(answer, handler=ns_type.handle_t_mx)
        # ret = ns_parse(answer, handler=ns_type.handle_bin)
        pprint([rr.contents for rr in ret])
        print()

Produces::

    Querying host 'gmail.com' type <ns_type.ns_t_ns: 2>:
    ['ns2.google.com', 'ns4.google.com', 'ns3.google.com', 'ns1.google.com']

    Querying host 'gmail.com' type <ns_type.ns_t_a: 1>:
    [bytearray(b'\xac\xd9\x11e')]

    Querying host 'gmail.com' type <ns_type.ns_t_mx: 15>:
    [(40, 'alt4.gmail-smtp-in.l.google.com'),
     (30, 'alt3.gmail-smtp-in.l.google.com'),
     (10, 'alt1.gmail-smtp-in.l.google.com'),
     (20, 'alt2.gmail-smtp-in.l.google.com'),
     (5, 'gmail-smtp-in.l.google.com')]

    Querying host 'gmail.com' type <ns_type.ns_t_txt: 16>:
    ['globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8=',
     'v=spf1 redirect=_spf.google.com']

    Querying host 'www.gmail.com' type <ns_type.ns_t_cname: 5>:
    ['mail.google.com']


2019-07-03: 0.2
~~~~~~~~~~~~~~~

- Renamed ``ns_type.handle_mx`` to ``ns_type.handle_t_mx``.
- Added:
  - ``handle_bin``
  - ``handle_compressed``
  - ``handle_text``
  - ``handle_t_cname``
  - ``handle_t_ns```
  - ``handle_t_txt```
- ``ns_parse`` now wraps the returned values into ``RR`` objects, so the
  type can be retrieved afterwards. The value can be fetched from its
  ``contents`` property.
- You can use ``handle_bin`` to fetch A or AAAA records.
- ``res_query`` now raises LookupError on failure.


2019-03-17: 0.1
~~~~~~~~~~~~~~~

- Initial release.


Copyright
---------

Copyright 2019, Walter Doekes (OSSO B.V.)

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see http://www.gnu.org/licenses/.
