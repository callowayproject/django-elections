===============
Candidate Model
===============

.. py:module:: elections.models

.. py:class:: Candidate

   A candidate running in an election

   .. py:attribute:: test_live
      
      **Required** ``CharField(1)``
      
      Single character flag indicating test (``t``) vs. live (``l``) election results data.

   .. py:attribute:: ap_candidate_id

      **Required** ``IntegerField`` *Primary Key*

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

   .. py:attribute:: politician_id

      ``IntegerField``

      National Politician ID(NPID). Uniquely assigned ID for this politician, regardless of the state or races in which this politician is a candidate.
      
      Field may be empty if no unique ID has been assigned to this politician.

