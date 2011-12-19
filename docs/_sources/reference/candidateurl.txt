==================
CandidateURL Model
==================

.. py:module:: elections.models

.. py:class:: CandidateURL

   URLs for each candidate.
   
   .. py:attribute:: candidate
      
      **Required** ``ForeignKey(`` :py:class:`Candidate` ``)``
      
      The :py:class:`Candidate` for this URL.
   
   .. py:attribute:: url
      
      ``CharField(255)``
      
   .. py:attribute:: description
      
      ``CharField(255)``
   
   .. py:attribute:: checksum
      
      **Required** ``CharField(32)``
      
      A calculated hash to see if imported data is different from the current data.