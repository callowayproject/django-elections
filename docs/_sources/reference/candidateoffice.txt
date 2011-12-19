=====================
CandidateOffice Model
=====================

.. py:module:: elections.models

.. py:class:: CandidateOffice

   An office a candidate currently holds or held in the past.

   .. py:attribute:: candidate
      
      **Required** ``ForeignKey(`` :py:class:`Candidate` ``)``
      
      The :py:class:`Candidate` that held or holds this office.
   
   .. py:attribute:: office_id
      
      ``CharField(1)``

      Single character office type ID. Only Top-of-the-ticket races (President [``P``], Governor [``G``], US Senate [``S``], and US House [``H``]) are guaranteed to be unique on a national level. All other office types are guaranteed to be unique only within a state. There are other characters used, depending on the state and local races.
      
      See also :py:attr:`CandidateOffice.office`
      
   .. py:attribute:: state
   
      ``CharField(2)``
      
      Two character state abbreviation (e.g., IA, LA, ). See also :py:attr:`CandidateOffice.state_name`
   
   .. py:attribute:: district_number
      
      ``CharField(4)``
      
      The district number for US House offices. See also :py:attr:`CandidateOffice.district_name`.
   
   .. py:attribute:: party_id

      ``CharField(16)``

      Party abbreviation for the race (e.g., Dem, GOP, Lib, etc.). See also :py:attr:`CandidateOffice.party_name`
   
   .. py:attribute:: status_id
      
      ``CharField(1)``
      
      The current status of the candidate in the office:
      
      * ``I`` Incumbant
      * ``C`` Challenger
      * ``Q`` Not seeking re-election
      
      See also :py:attr:`CandidateOffice.status_description`
   
   .. py:attribute:: office
      
      ``CharField(64)``
      
      The full name of the office.
   
   .. py:attribute:: state_name
      
      ``CharField(100)``
      
      The full name of the state in which this office resides.
   
   .. py:attribute:: district_name
      
      ``CharField(32)``
      
      The full name of the district for US House offices.
   
   .. py:attribute:: party_name
      
      ``CharField(32)``
      
      The full name of the candidate's party
   
   .. py:attribute:: office_description
      
      ``CharField(64)``
      
      A description of the office.
   
   .. py:attribute:: status_description
      
      ``CharField(64)``
      
      The full text of the status of the candidate in the office.
   
   .. py:attribute:: next_election
      
      ``IntegerField``
      
      The year in which the candidate is up for re-election.
   
   .. py:attribute:: checksum
      
      **Required** ``CharField(32)``
      
      A calculated hash to see if imported data is different from the current data.