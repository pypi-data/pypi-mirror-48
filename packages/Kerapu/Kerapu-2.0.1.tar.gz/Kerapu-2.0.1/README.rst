Kerapu
======

Een implementatie van de Grouper in Python voor Business Intelligence doeleinden.

+----------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Social                                                                                                                     | Legal                                                                   | Release                                        | Tests                                                                                   | Code                                                                                                   |
+============================================================================================================================+=========================================================================+================================================+=========================================================================================+========================================================================================================+
| .. image:: https://badges.gitter.im/SetBased/py-kerapu.svg                                                                 | .. image:: https://img.shields.io/github/license/setbased/py-kerapu.svg | .. image:: https://badge.fury.io/py/Kerapu.svg | .. image:: https://travis-ci.org/SetBased/py-kerapu.svg?branch=master                   | .. image:: https://scrutinizer-ci.com/g/SetBased/py-kerapu/badges/quality-score.png?b=master           |
|   :target: https://gitter.im/SetBased/py-kerapu?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge  |   :target: https://opensource.org/licenses/MIT                          |   :target: https://badge.fury.io/py/Kerapu     |   :target: https://travis-ci.org/SetBased/py-kerapu                                     |   :target: https://scrutinizer-ci.com/g/SetBased/py-kerapu/?branch=master                              |
|                                                                                                                            |                                                                         |                                                | .. image:: https://scrutinizer-ci.com/g/SetBased/py-kerapu/badges/coverage.png?b=master |                                                                                                        |
|                                                                                                                            |                                                                         |                                                |   :target: https://scrutinizer-ci.com/g/SetBased/py-kerapu/?branch=master               |                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

Installatie
===========

Kerapu kan eenvoudig geïnstalleerd worden met pip:

.. code:: sh

    pip3 install kerapu

Voorbereiding
=============

Alvorens gebruik te kunnen maken van Kerapu moeten de boombestanden en referentietabellen worden geconverteerd en opgeslagen. Ten tijde van schrijven van dit document was de meest recente versie van Grouper Tabellen ``v20180920``, vervang in de onderstaande tekst deze versie voor de meest recente versie.

* Download het bestand ``Grouper Tabellen v20180920`` van https://puc.overheid.nl/nza/doc/PUC_259930_22/.
* Extract de XML-bestanden uit het ZIP-bestand:

.. code:: sh

   unzip -x "20190101 Groupertabellen v20180920.zip"

* Converteer de XML-bestanden naar CSV (in het voorbeeld hieronder worden de CSV-bestanden weggeschreven in de folder ``var/lib``):

.. code:: sh

   kerapu kerapu:shredder "20190101 BoomBestanden v20180920.xml" var/lib/
   kerapu kerapu:shredder "20190101 Referenties v20180920.xml" var/lib/

Voorbeeld
=========

Hieronder een voorbeeld om de zorgproductcode van een subtraject af te leiden.

.. code:: python

   from kerapu.Kerapu import Kerapu
   from kerapu.lbz.Subtraject import Subtraject

   # Maak een Grouper object en laad boombestanden en referentietabellen.
   grouper = Kerapu()
   grouper.init_static('var/lib')

   # Maak een subtraject object.
   subtraject = Subtraject('1',             # Subtrajectnummer
                           '0303',          # Zorgverlenerspecificatiecode
                           '0280',          # Diagnosecode
                           '11',            # Zorgtypecode
                           '000',           # Zorgvraagcode
                           '2012-01-01',    # Begindatum subtraject
                           '2000-01-01',    # Geboortedatum
                           'M',             # Geslachtscode
                           '01234567')      # AGB-code zorginstelling

   # Voeg uitgevoerde zorgactiviteiten aan het subtraject toe.
   subtraject.add_zorg_activiteit('038940', 1)
   subtraject.add_zorg_activiteit('038941', 1)
   subtraject.add_zorg_activiteit('190012', 1)
   subtraject.add_zorg_activiteit('190015', 1)

   # Bepaal zorgproductgroep en zorgproduct.
   zorg_product_code = grouper.bepaal_zorg_product(subtraject)

   print('Zorgproductgroepcode: {}'.format(subtraject.zorg_product_groep_code))
   print('Zorgproductcode: {}'.format(subtraject.zorg_product_code))

Testset
=======

De grouperbestanden bevatten sinds 2019 een testset. Deze testset is terug te vinden in bestand ``var/lib/testset.csv`` en zijn een onderdeel van de unittesten van Kerapu.

Het commando voor het converteren van de XML-bestanden met test data is:

.. code:: sh

   ./bin/kerapu kerapu:test-shredder ~/Downloads/20190101\ Testset\ Grouper\ RZ19b\ v20180920.zip  test/var/lib/testset.csv

Ondersteuning en bijdragen
==========================

Ondersteuning is beschikbaar via GitHub tickets, Gitter_ en email: support@setbased.nl.

Bijdragen zijn uiteraard welkom, we werken volgens de GitHub Flow, zie de handleiding_ voor het maken een pull request.

.. _Gitter: https://gitter.im/SetBased/py-kerapu
.. _handleiding: https://guides.github.com/introduction/flow/

Wie gebruiken Kerapu?
=====================

.. image:: https://avatars0.githubusercontent.com/u/12200736?v=3&s=200
  :height: 100px
  :width: 100px
  :target: https://github.com/NLHEALTHCARE/

Licentie
========

Dit project is gelicentieerd onder de MIT-licentie.
