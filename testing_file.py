from dataset_generator import *
from tree_generation_algorithms import *
import time
import random

dataset_generator("4_2000", four_letter_alphabet, 2000)
dataset_generator("8_2000", eight_letter_alphabet, 2000)
dataset_generator("12_2000", twelve_letter_alphabet, 2000)
dataset_generator("4_5000", four_letter_alphabet, 5000)
dataset_generator("8_5000", eight_letter_alphabet, 5000)
dataset_generator("12_5000", twelve_letter_alphabet, 5000)

first = open("4_2000").read()
second = open("8_2000").read()
third = open("12_2000").read()
fourth = open("4_5000").read()
fifth = open("8_5000").read()
sixth = open("12_5000").read()


def generate_motifs(text, number_of_keywords, keyword_size):
    keywords = []
    for i in range(number_of_keywords):
        start = random.randint(0, len(text) - keyword_size - 1)
        keywords.append(text[start:start + keyword_size])
    return keywords


def easy_dataset_small_keywords():
    simulation_start_time = time.time()
    print("easy_dataset_small_keywords started at : " , simulation_start_time)
    motifs = generate_motifs(first, 4,  3)
    naive_build_start = time.time()
    naive_suffix_tree = keyword_construction("4_2000", Tree())
    naive_build_end = time.time()
    print("Naive Suffix Build Time: ", naive_build_end - naive_build_start)
    optimized_suffix_tree = SuffixTree(first)
    optimized_end = time.time()
    print("Optimized Tree Build Time : ", optimized_end - naive_build_end)
    keyword_tree = build_keyword_tree(motifs)
    keyword_tree_construction_end = time.time()
    print("Keyword Tree Build Time : ", keyword_tree_construction_end - optimized_end)
    naive_start = time.time()
    print(motifs)
    for index in range(len(motifs)):
        tree_lookup(naive_suffix_tree.root, motifs[index])
    naive_end = time.time()
    print("Naive Suffix Tree Found All Motifs in : ", naive_start - naive_end)

    optimized_start = time.time()
    for index in range(len(motifs)):
        optimized_suffix_tree.find(motifs[index])
    optimized_end = time.time()
    print("Optimized Suffix Tree Found All Motifs in : ", optimized_end - optimized_start)
    keyword_start = time.time()
    find_in_dataset("4_2000", keyword_tree)
    keyword_end = time.time()
    print("Keyword Tree Found All Motifs in : ", keyword_end - keyword_start)

easy_dataset_small_keywords()

def easy_dataset_large_keywords():
    simulation_start_time = time.time()
    print("easy_dataset_large_keywords started at : " , simulation_start_time)
    motifs = generate_motifs(first, 4,  6)
    naive_build_start = time.time()
    naive_suffix_tree = keyword_construction("4_2000", Tree())
    naive_build_end = time.time()
    print("Naive Suffix Build Time: ", naive_build_end - naive_build_start)
    optimized_suffix_tree = SuffixTree(first)
    optimized_end = time.time()
    print("Optimized Tree Build Time : ", optimized_end - naive_build_end)
    keyword_tree = build_keyword_tree(motifs)
    keyword_tree_construction_end = time.time()
    print("Keyword Tree Build Time : ", keyword_tree_construction_end - optimized_end)
    naive_start = time.time()
    print(motifs)
    for index in range(len(motifs)):
        tree_lookup(naive_suffix_tree.root, motifs[index])
    naive_end = time.time()
    print("Naive Suffix Tree Found All Motifs in : ", naive_end - naive_start)

    optimized_start = time.time()
    for index in range(len(motifs)):
        optimized_suffix_tree.find(motifs[index])
    optimized_end = time.time()
    print("Optimized Suffix Tree Found All Motifs in : ", optimized_end - optimized_start)
    keyword_start = time.time()
    find_in_dataset("4_2000", keyword_tree)
    keyword_end = time.time()
    print("Keyword Tree Found All Motifs in : ", keyword_end - keyword_start)

print(" ")
print(" ")
easy_dataset_large_keywords()
print(" ")
print(" ")
def four_five_small_keywords():
    simulation_start_time = time.time()
    print("four_five_small_keywords started at : " , simulation_start_time)
    motifs = generate_motifs(first, 6,  3)
    naive_build_start = time.time()
    naive_suffix_tree = keyword_construction("4_5000", Tree())
    naive_build_end = time.time()
    print("Naive Suffix Build Time: ", naive_build_end - naive_build_start)
    optimized_suffix_tree = SuffixTree(second)
    optimized_end = time.time()
    print("Optimized Tree Build Time : ", optimized_end - naive_build_end)
    keyword_tree = build_keyword_tree(motifs)
    keyword_tree_construction_end = time.time()
    print("Keyword Tree Build Time : ", keyword_tree_construction_end - optimized_end)
    naive_start = time.time()
    print(motifs)
    for index in range(len(motifs)):
        tree_lookup(naive_suffix_tree.root, motifs[index])
    naive_end = time.time()
    print("Naive Suffix Tree Found All Motifs in : ", naive_end - naive_start)

    optimized_start = time.time()
    for index in range(len(motifs)):
        optimized_suffix_tree.find(motifs[index])
    optimized_end = time.time()
    print("Optimized Suffix Tree Found All Motifs in : ", optimized_end - optimized_start)
    keyword_start = time.time()
    find_in_dataset("4_5000", keyword_tree)
    keyword_end = time.time()
    print("Keyword Tree Found All Motifs in : ", keyword_end - keyword_start)

four_five_small_keywords()
print("")
print("")

def four_five_large_keywords():
    simulation_start_time = time.time()
    print("four_five_large_keywords started at : " , simulation_start_time)
    motifs = generate_motifs(second, 20,  500)
    naive_build_start = time.time()
    naive_suffix_tree = keyword_construction("4_5000", Tree())
    naive_build_end = time.time()
    print("Naive Suffix Build Time: ", naive_build_end - naive_build_start)
    optimized_suffix_tree = SuffixTree(second)
    optimized_end = time.time()
    print("Optimized Tree Build Time : ", optimized_end - naive_build_end)
    keyword_tree = build_keyword_tree(motifs)
    keyword_tree_construction_end = time.time()
    print("Keyword Tree Build Time : ", keyword_tree_construction_end - optimized_end)
    naive_start = time.time()
    #print(motifs)
    for index in range(len(motifs)):
        tree_lookup(naive_suffix_tree.root, motifs[index])
    naive_end = time.time()
    print("Naive Suffix Tree Found All Motifs in : ", naive_end - naive_start)

    optimized_start = time.time()
    for index in range(len(motifs)):
        optimized_suffix_tree.find(motifs[index])
    optimized_end = time.time()
    print("Optimized Suffix Tree Found All Motifs in : ", optimized_end - optimized_start)
    keyword_start = time.time()
    find_in_dataset("4_5000", keyword_tree)
    keyword_end = time.time()
    print("Keyword Tree Found All Motifs in : ", keyword_end - keyword_start)

#four_five_large_keywords()
print("")
print("")
def four_five_large_keywords_many_motifs():
    simulation_start_time = time.time()
    print("four_five_large_keywords_many_motifs started at : " , simulation_start_time)
    motifs = generate_motifs(second, 2000,  14)
    naive_build_start = time.time()
    naive_suffix_tree = keyword_construction("4_5000", Tree())
    naive_build_end = time.time()
    print("Naive Suffix Build Time: ", naive_build_end - naive_build_start)
    optimized_suffix_tree = SuffixTree(second)
    optimized_end = time.time()
    print("Optimized Tree Build Time : ", optimized_end - naive_build_end)
    keyword_tree = build_keyword_tree(motifs)
    keyword_tree_construction_end = time.time()
    print("Keyword Tree Build Time : ", keyword_tree_construction_end - optimized_end)
    naive_start = time.time()
    #print(motifs)
    for index in range(len(motifs)):
        tree_lookup(naive_suffix_tree.root, motifs[index])
    naive_end = time.time()
    print("Naive Suffix Tree Found All Motifs in : ", naive_end - naive_start)

    optimized_start = time.time()
    for index in range(len(motifs)):
        optimized_suffix_tree.find(motifs[index])
    optimized_end = time.time()
    print("Optimized Suffix Tree Found All Motifs in : ", optimized_end - optimized_start)
    keyword_start = time.time()
    find_in_dataset("4_5000", keyword_tree)
    keyword_end = time.time()
    print("Keyword Tree Found All Motifs in : ", keyword_end - keyword_start)

#four_five_large_keywords_many_motifs()

print("")
print("")
def eight_two_large_keywords():
    simulation_start_time = time.time()
    print("eight_two_large_keywords started at : " , simulation_start_time)
    motifs = generate_motifs(third, 2000, 40)
    naive_build_start = time.time()
    naive_suffix_tree = keyword_construction("8_2000", Tree())
    naive_build_end = time.time()
    print("Naive Suffix Build Time: ", naive_build_end - naive_build_start)
    optimized_suffix_tree = SuffixTree(third)
    optimized_end = time.time()
    print("Optimized Tree Build Time : ", optimized_end - naive_build_end)
    keyword_tree = build_keyword_tree(motifs)
    keyword_tree_construction_end = time.time()
    print("Keyword Tree Build Time : ", keyword_tree_construction_end - optimized_end)
    naive_start = time.time()
    #print(motifs)
    for index in range(len(motifs)):
        tree_lookup(naive_suffix_tree.root, motifs[index])
    naive_end = time.time()
    print("Naive Suffix Tree Found All Motifs in : ", naive_end - naive_start)

    optimized_start = time.time()
    for index in range(len(motifs)):
        optimized_suffix_tree.find(motifs[index])
    optimized_end = time.time()
    print("Optimized Suffix Tree Found All Motifs in : ", optimized_end - optimized_start)
    keyword_start = time.time()
    find_in_dataset("8_2000", keyword_tree)
    keyword_end = time.time()
    print("Keyword Tree Found All Motifs in : ", keyword_end - keyword_start)

#eight_two_large_keywords()
print("")
print("")
def twelve_two_large_keywords_many_motifs():
    simulation_start_time = time.time()
    print("eight_two_large_keywords_many_motifs started at : " , simulation_start_time)
    motifs = generate_motifs(fifth, 30,  800)
    naive_build_start = time.time()
    naive_suffix_tree = keyword_construction("12_2000", Tree())
    naive_build_end = time.time()
    print("Naive Suffix Build Time: ", naive_build_end - naive_build_start)
    optimized_suffix_tree = SuffixTree(fifth)
    optimized_end = time.time()
    print("Optimized Tree Build Time : ", optimized_end - naive_build_end)
    keyword_tree = build_keyword_tree(motifs)
    keyword_tree_construction_end = time.time()
    print("Keyword Tree Build Time : ", keyword_tree_construction_end - optimized_end)
    naive_start = time.time()
    #print(motifs)
    for index in range(len(motifs)):
        tree_lookup(naive_suffix_tree.root, motifs[index])
    naive_end = time.time()
    print("Naive Suffix Tree Found All Motifs in : ", naive_end - naive_start)

    optimized_start = time.time()
    for index in range(len(motifs)):
        optimized_suffix_tree.find(motifs[index])
    optimized_end = time.time()
    print("Optimized Suffix Tree Found All Motifs in : ", optimized_end - optimized_start)
    keyword_start = time.time()
    find_in_dataset("12_2000", keyword_tree)
    keyword_end = time.time()
    print("Keyword Tree Found All Motifs in : ", keyword_end - keyword_start)


twelve_two_large_keywords_many_motifs()