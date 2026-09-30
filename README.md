# OS Lab — Linux / Ubuntu (Python)

**Operating Systems lab experiments in Python** — system calls, CPU scheduling, synchronization, deadlock, memory management, and file systems — organized by lab and question.

> Course submission repo. Two assignment PDFs are included for reference.

---

## Layout

```
Operating-Systems-Lab/
  program1.py            # system calls
  program2.py            # FCFS / SJF scheduling
  program3.py            # priority + round robin
  requirements.txt
  Lab1/  Q1_System_Calls · Q2_FCFS_SJF · Q3_Priority_Round_Robin · Q4_Metrics_Threads_IPC
  Lab2/  Q1_Thread_Models · Q2_Race_Mutex_Semaphore · Q3_Classical_Synchronization · Q4_Deadlock_Banker
  Lab3/  Q1_Contiguous_Swapping · Q2_Paging_Segmentation · Q3_Page_Replacement
         Q4_Device_Management · Q5_Disk_Scheduling
  Lab4/  Q1_File_Operations · Q2_Direct_Indexed_Directory
         Q3_File_Allocation · Q4_Free_Space_Permissions
OS-First-Program/   program1.py
OS-Second-Program/  program2.py
OS-Third-Program/   program3.py
OS-Fourth-Program/  program4.py (+ test_file.txt)
```

Each `Lab*/Q*/` folder contains its per-question README (currently scaffolded — content being filled in).

## Run

```bash
git clone https://github.com/Tusharkapoor-oop/OS_LAB_Linux_Ubantu.git
cd OS_LAB_Linux_Ubantu
pip install -r Operating-Systems-Lab/requirements.txt

python Operating-Systems-Lab/program1.py    # system calls demo
python Operating-Systems-Lab/program2.py    # FCFS / SJF
python Operating-Systems-Lab/program3.py    # priority / round robin
python OS-Fourth-Program/program4.py        # file-system exercise
```

## Known issues (tracked, not hidden)

- The root-level PDFs are duplicates of the ones inside `Operating-Systems-Lab/` — de-duplication needs owner approval (nothing will be deleted without it).
- Assignment PDF filenames contain an enrollment number; anonymised filenames planned.
- 17 scaffolded `README.md` files are currently 0 bytes — they will be filled question-by-question.
- Several programs exist in two locations (`program2.py` in three) — consolidation planned.

## License

No license file yet — coursework, MIT intended (to be added by the repository owner).
