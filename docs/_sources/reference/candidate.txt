===============
Candidate Model
===============

.. py:module:: elections.models

.. py:class:: Candidate

   A candidate running in an election

   
   .. py:attribute:: test_live
      
      **Required** ``CharField(1)``
      
      Single character flag indicating test (``t``) vs. live (``l``) election results data.

   .. py:attribute:: politician_id

      ``IntegerField`` *Primary Key*

      National Politician ID(NPID). Uniquely assigned ID for this politician, regardless of the state or races in which this politician is a candidate.

      Field may be empty if no unique ID has been assigned to this politician.

   .. py:attribute:: ap_candidate_id

      **Required** ``IntegerField`` *Unique*

      AP-assigned unique ID identifying this specific candidate.

   .. py:attribute:: candidate_number

      **Required** ``IntegerField``

      AP defined candidate number. Candidate numbers are guaranteed unique only within a single state. See :py:attr:`Candidate.politician_id` field below for the unique candidate number/ID at the National level, if available.

   .. py:attribute:: first_name

      ``CharField(64)``

      Candidate's first name.

   .. py:attribute:: middle_name

      ``CharField(64)``

      Candidate's middle name.

   .. py:attribute:: last_name

      ``CharField(64)``

      Candidate's last name.

   .. py:attribute:: junior

      ``CharField(16)``

      Trailing Jr or Sr, etc.

   .. py:attribute:: use_junior

      **Required** ``BooleanField`` *default:* ``False``

      Flag indicating whether The AP appends the junior suffix to the candidate's name in reports.

   .. py:attribute:: year_first_elected
   
      ``IntegerField``
      
      The year the candidate was first elected to their current office.

   .. py:attribute:: birth_date

      ``DateField``

      The candidate's birth date

   .. py:attribute:: birth_place
   
      ``CharField(100)``
      
      The name of the place of the candidate's birth.
   
   .. py:attribute:: birth_state
      
      ``CharField(2)``
      
      The two-letter state abbreviation of the state in which the candidate was born (If in the United States).
   
   .. py:attribute:: birth_province
      
      ``CharField(100)``
      
      The name of the province in which the candidate was born (If outside the United States).
   
   .. py:attribute:: birth_country
      
      ``CharField(100)``
      
      The name of the country in which the candidate was born.
   
   .. py:attribute:: residence_place
      
      ``CharField(100)``
      
      The name of the place in which the candidate currently lives.
   
   .. py:attribute:: residence_state
      
      ``CharField(2)``
      
      The two-letter state abbreviation in which the candidate currently resides.
   
   .. py:attribute:: gender
      
      ``CharField(1)``
      
      Either ``M`` for male, or ``F`` for female.
   
   .. py:attribute:: ethnicity
      
      ``CharField(100)``
      
      The candidate's ethnicity
   
   .. py:attribute:: hispanic
      
      ``CharField(100)``
      
      The candidate's hispanic background
   
   .. py:attribute:: religion
      
      ``CharField(100)``
      
      The candidate's declared practiced religion.
   
   .. py:attribute:: biography
      
      ``TextField``
      
      A simple biographical narrative of the candidate.
   
   .. py:attribute:: profile
      
      ``TextField``
      
      A political profile of the candidate.
   
   .. py:attribute:: campaigns
      
      ``TextField``
      
      Brief information about current election campaigns.
   
   .. py:attribute:: timestamp
      
      **Required** ``DateTime``
      
      When the information was last modified.

Properties
==========


.. py:attribute:: Candidate.full_name
   
   The candidate's full name, formatted correctly depending on the existence of a middle name and junior suffix.


Related Objects
===============


.. py:attribute:: Candidate.offices
   
   Access to all related :py:class:`CandidateOffice` records.

.. py:attribute:: Candidate.education
   
   Access to all related :py:class:`CandidateEducation` records.

.. py:attribute:: Candidate.phones
   
   Access to all the :py:class:`CandidatePhone` records.

.. py:attribute:: Candidate.urls
   
   Access to all the :py:class:`CandidateURL` records.

