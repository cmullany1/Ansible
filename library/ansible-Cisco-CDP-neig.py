---
- hosts: all
  conenction: local
  gather_facts: no
		
  tasks:
  - name: Get CDP neighbor
    command: cdp neig