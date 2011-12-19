====================
CandidatePhone Model
====================

.. py:module:: elections.models

.. py:class:: CandidatePhone

   Contact phone numbers for each candidate.
   
   .. py:attribute:: candidate
      
      **Required** ``ForeignKey(`` :py:class:`Candidate` ``)``
      
      The :py:class:`Candidate` for this phone number.
   
   .. py:attribute:: phone_number
      
      ``CharField(15)``
      
   .. py:attribute:: extension
      
      ``CharField(10)``
   
   .. py:attribute:: location
      
      ``CharField(64)``
   
   .. py:attribute:: detail
      
      ``CharField(64)``
   
   .. py:attribute:: checksum
      
      **Required** ``CharField(32)``
      
      A calculated hash to see if imported data is different from the current data.