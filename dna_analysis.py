# Name: Yichun Zhou
# PROG for BA
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print ("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0 # Q4, Number of A and T nucleotides seen so far.

#Q5 Number of each nucleotide seen so far.
g_count = 0
c_count = 0
a_count = 0
t_count = 0
# For caculating a_count + t_count + c_count + g_count
sum_atcg = 0
# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
        
        # Q4 if the bp is a A or a T,
    if bp == 'A' or bp == 'T':
        # increment the count of at
        at_count = at_count + 1

    # Q5 if the bp is a G, etc...
    if bp == 'G':
        # increment the count of g
        g_count = g_count + 1
    if bp == 'C':
        c_count = c_count + 1
    if bp == 'A':
        a_count = a_count + 1
    if bp == 'T':
        t_count = t_count + 1

sum_atcg = a_count + t_count + c_count + g_count
# divide the gc_count by the total_count
gc_content = float(gc_count) / sum_atcg

# Print the answer
print ('GC-content:', gc_content)

# Q4 divide the ac_count by the total_count
at_content = float(at_count) / sum_atcg

# Print the answer
print ('AT-content:', at_content)

# Q5 count each necleotides
print ('G count:', g_count)
print ('C count:', c_count)
print ('A count:', a_count)
print ('T count:', t_count)

#Q6 get 3 quantities, sum of (a,c,g,t); total count; len(seq)
print ('Sum count:', str(sum_atcg))
print ('Total count:', str(total_count))
print ('seq length:', str(len(seq)))

#Q7 AT/GC Ratio
at_gc_ratio = (float(a_count) + float(t_count))/ (float(g_count) + float(c_count))
print ('AT/GC Ratio:', at_gc_ratio)

#Q8 categorize GC Content
# caculate gc/sum of (a,c,g,t)
cat_gc_content = (g_count + c_count) / sum_atcg
# if above 60%
if (cat_gc_content > 0.6 ):
    print("high GC content")
# if lower than 40%
elif (cat_gc_content < 0.4 ):
    print("low GC content")
#between 40%-60%
else :
    print("moderate GC content")


