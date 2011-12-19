========================
CandidateEducation Model
========================

.. py:module:: elections.models

.. py:class:: CandidateEducation

   Post-secondary education received for each candidate.
   
   .. py:attribute:: candidate
      
      **Required** ``ForeignKey(`` :py:class:`Candidate` ``)``
      
      The :py:class:`Candidate` that held or holds this office.
   
   .. py:attribute:: school_name
      
      ``CharField(64)``
      
      The full name of the school or institution.
   
   .. py:attribute:: school_type
      
      ``CharField(64)``
      
      Typically ``Undergraduate`` or ``Graduate``.
   
   .. py:attribute:: major
      
      ``CharField(64)``
      
      The subject studied at the institution.
   
   .. py:attribute:: degree
      
      ``CharField(64)``
      
      The initials of the degree earned, or ``Attended``.
   
   .. py:attribute:: school_city
      
      ``CharField(100)``
      
      The name of the city in which the institution resides.
   
   .. py:attribute:: school_state
      
      ``CharField(2)``
      
      The two-letter abbreviation for the state in which the institution resides (for US-based institutions).
   
   .. py:attribute:: school_province
      
      ``CharField(100)``
      
      The name of the province in which the institution resides (for non-US-based institutions).
   
   .. py:attribute:: school_country
      
      ``CharField(64)``
      
      The country in which the institution resides.
   
   .. py:attribute:: checksum
      
      **Required** ``CharField(32)``
      
      A calculated hash to see if imported data is different from the current data.