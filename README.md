# Assessment Recommendation Engine

## Overview
This project implements a content-based recommendation system that suggests suitable SHL-style assessments based on job role, required skills, and experience level.

The goal is to help organizations choose the most relevant assessments for different roles using machine learning techniques.

---

## Problem Statement
Given a catalogue of assessments, recommend the most appropriate assessments for a candidate or job role based on textual similarity between job requirements and assessment descriptions.

---

## Dataset
A sample assessment catalogue was created containing:
- Assessment name
- Job role
- Required skills
- Experience level
- Description

The dataset is stored in:
Add this section (copy-paste):

This project implements a GenAI-based Assessment Recommendation Engine using a Retrieval-Augmented Generation (RAG) pipeline. The system scrapes SHL’s publicly available product catalog, stores it in a structured format, generates semantic embeddings using sentence-transformers, and retrieves relevant assessments via FAISS. A lightweight evaluation strategy is included to measure recommendation effectiveness.