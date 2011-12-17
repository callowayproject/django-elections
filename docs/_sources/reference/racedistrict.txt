==================
RaceDistrict Model
==================

.. py:module:: elections.models

.. py:class:: RaceDistrict

   Each ``RaceDistrict`` object contains either the information associated with a particular race in a particular district of a state, or the statewide district summary for that race.

   .. py:attribute:: test_live
      
      **Required** ``CharField(1)``
      
      Single character flag indicating test (``t``) vs. live (``l``) election results data.

   .. py:attribute:: race_district_id
      
      **Required** ``BigIntegerField`` *Primary Key*
      
      The race_county_id value is for use as a unique identifier for reference from the :py:class:`DistrictResult` model.

   .. py:attribute:: race_number

      **Required** ``IntegerField``

      AP-assigned race number. Race numbers are guaranteed to be unique only within a state.

   .. py:attribute:: election_date

      **Required** ``DateField``

      Date of the election.

   .. py:attribute:: state_postal

      **Required** ``CharField(2)``

      Two character state abbreviation (e.g., IA, LA, ).

   .. py:attribute:: district_type

      ``CharField(16)``

      Abbreviation of the district type
      
      * **AL** At-large delegate
      * **PL** PLEO delegate
      * **CD** Congressional District
      * **DD** Delegate District
      * **SD** State Senate District


   .. py:attribute:: cd_number

      ``IntegerField``

      A unique district ID with one (1) indicating statewide summaries.

   .. py:attribute:: district_name

      ``CharField(64)``

      Name of the district (e.g., CD 4, At-Large, etc.)

   .. py:attribute:: office_id

      **Required** ``CharField(1)``

      Single character office type ID. Only Top-of-the-ticket races (President [``P``], Governor [``G``], US Senate [``S``], and US House [``H``]) are guaranteed to be unique on a national level. All other office types are guaranteed to be unique only within a state. There are other characters used, depending on the state and local races.

   .. py:attribute:: race_type_id

      **Required** ``CharField(1)``

      National, state or local race type identifier. National identifiers are:

      * ``D``: Dem Primary
      * ``E``: Dem Caucus
      * ``R``: GOP Primary
      * ``S``: GOP Caucus
      * ``G``: General

      Other characters may be used, depending on the state and local races.

   .. py:attribute:: seat_number

      **Required** ``IntegerField``

      Integer indicating district number or an initiative number. This may be zero (0) for a statewide race.

   .. py:attribute:: office_name

      ``CharField(64)``

      Name of the office (e.g., U.S. House, Governor, etc.).

   .. py:attribute:: seat_name

      ``CharField(64)``

      The district or initiative name (e.g., District 46, 1A-Gay Marriage, etc.) This may be empty for a statewide race (e.g., a Governor race).

   .. py:attribute:: race_type_party

      ``CharField(16)``

      Party abbreviation for the race (e.g., Dem, GOP, Lib, etc.). This may be empty for a General Election.

   .. py:attribute:: race_type

      ``CharField(32)``

      Description of the type of race (e.g., Primary, Runoff, General).

   .. py:attribute:: office_description

      ``CharField(64)``

      Further description of the office type.

   .. py:attribute:: number_of_winners

      **Required** ``IntegerField()``

      The maximum number of winners.

   .. py::attribute:: number_in_runoff

      ``IntegerField``

      Number of candidates in a runoff race.

   .. py:attribute:: precincts_reporting

      **Required** ``IntegerField``

      The number of precincts currently reporting during the election.

   .. py:attribute:: total_precincts

      **Required** ``IntegerField``

      The total number of precincts.