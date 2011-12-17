==================
CountyResult Model
==================

.. py:module:: elections.models

.. py:class:: CountyResult

   Each  ``CountyResult`` object describes the result for a particular ``Candidate`` in a particular ``RaceCounty``.

   .. py:attribute:: test_live
      
      **Required** ``CharField(1)``
      
      Single character flag indicating test (``t``) vs. live (``l``) election results data.

   .. py:attribute:: race_county

      **Required** ``ForeignKey(`` :py:class:`RaceCounty` ``)``

      Foreign key to a :py:class:`RaceCounty` object.

   .. py:attribute:: ap_candidate

      **Required** ``ForeignKey(`` :py:class:`Candidate` ``)``

      Foreign key to a :py:class:`Candidate` object.

   .. py:attribute:: party

      ``CharField(16)``

      The candidate's party abbreviation. This may be different than the ``CountyResult.race_county.race_type_party`` field.

   .. py:attribute:: incumbent

      **Required** ``BooleanField`` *default:* ``False``

      ``True`` means the candidate an incumbent.

   .. py:attribute:: vote_count

      **Required** ``IntegerField`` *default:* ``0``

      Candidate's or an initiative’s vote tally.

   .. py:attribute:: winner

      ``CharField(1)``

      ``X`` means candidate is the winner or the initiative received a final Yes or No vote, ``R`` means candidate advances to the runoff election. An empty value indicates a non-winner

   .. py:attribute:: natl_order

      ``IntegerField``

      Winning order of candidate in national system.
