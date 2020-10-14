# -*- coding: utf-8 -*-
"""
author: JDarlow2020
"""
#     Unfinished code - this code is a work in progress and may not work on test data until completed.

def ballgown_parser(results, IDs, Names):
    '''
    This ballgown_parser script parses Ballgown output into CSV files \
    which contain the gene/transcript names and their associated \
    differential expression statistics.
    
    Three CSV files must be provided to this script:
    results - the results csv file for a given factor, generated from Ballgown
    IDs - the geneIDs or transcriptIDs csv file, generated from Ballgown
    Names - the geneNames or transcriptNames csv files, generated from Ballgown
    '''
    #%%
    sig_gene_MSTRG = []
    with open(results, "r") as csv:
        content = csv.readlines()
        content = content[1:]
        for line in content:
            if float(line.split(",")[-1]) < 0.05:
                sig_gene_MSTRG.append(line.split(",")[1])
            else:
                break
    #print(sig_gene_MSTRG[:5])
    print(len(sig_gene_MSTRG))
    def rm_sm(lst):
        new = []
        for i in lst:
            new.append(i.strip("\""))
        return new
    sig_gene_MSTRG = rm_sm(sig_gene_MSTRG)
    #print(sig_gene_MSTRG[:5])
    #%%
    with open(IDs, "r") as csv:
        content = csv.readlines()
        #print(content[:5])
        content2 = []
        for i in content:
            content2.append(i.strip("\n").strip("\"").strip(","))
        #print(content2[:5])
        #print((content2[2]))
        content3 = []
        for i in content2[1:]:
            content3.append(i.split("\",\""))
        #print(content3[:5])
        MSTRG_id = []
        for i in sig_gene_MSTRG:
            for k in content3:
                if i in k:
                    MSTRG_id.append(k)  
    #%%                
    #print(MSTRG_id[:5])      
    IDs = []
    for i in MSTRG_id:
        IDs.append(i[0])
    #print(len(MSTRG_id))
    MSTRG_id2 = MSTRG_id
    #%%
    with open("Names.csv", "r") as csv:
        content = csv.readlines()
        content2 = []
        for i in content:
            content2.append(i.strip("\n").strip("\"").strip(","))
        content3 = []
        for i in content2[1:]:
            content3.append(i.split("\",\""))
        #print(content3[0])
        content4 = []
        for i in content3:
            content4.append(i[1])
        count = 0
        for i in IDs:
            MSTRG_id2[count].append(content4[int(i)-1])
            count += 1
    #%%
    #print(MSTRG_id2[:5])
    #print(IDs[:5])
    #print(MSTRG_id2[:5])
    #print(content4[:5])
    #%%
    with open("get_sig_gene.csv", "w") as output:
        output.write("gene_id" + "," + "MSTRG" + "," + "Gene Name" + "\n")
        for i in MSTRG_id:
            output.write(str(i[0]) + "," + str(i[1] + "," + str(i[2]) + "\n"))
    
    ######## get_sig_gene.csv written
    #%%
    # Convert dots to MSTRGs
    temp = []
    with open("get_sig_gene.csv", "r") as csv:
        for line in csv:
            if line.split(",")[2] == ".\n":
                temp.append([line.split(",")[0], line.split(",")[1], str(line.split(",")[1]) + "\n"])
            else:
                temp.append(line.split(","))
    
    with open("get_sig_gene_no_dots.csv", "w") as csv:
        for i in temp:
            csv.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]))
    
    #%%
    # Create list of names based on MSTRG 
    names = []
    with open("D:\Data\get_sig_gene_no_dots.csv", "r") as csv:
        csv = csv.readlines()
        for i in range(len(csv)-10):
            if csv[i].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i].split(",")[2])
            elif csv[i+1].split(",")[1] == csv[i].split(",")[1] and csv[i+1].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+1].split(",")[2])
            elif csv[i+2].split(",")[1] == csv[i].split(",")[1] and csv[i+2].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+2].split(",")[2])
            elif csv[i+3].split(",")[1] == csv[i].split(",")[1] and csv[i+3].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+3].split(",")[2])
            elif csv[i+4].split(",")[1] == csv[i].split(",")[1] and csv[i+4].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+4].split(",")[2])
            elif csv[i+5].split(",")[1] == csv[i].split(",")[1] and csv[i+5].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+5].split(",")[2])
            elif csv[i+6].split(",")[1] == csv[i].split(",")[1] and csv[i+6].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+6].split(",")[2])
            elif csv[i+7].split(",")[1] == csv[i].split(",")[1] and csv[i+7].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+7].split(",")[2])
            elif csv[i+8].split(",")[1] == csv[i].split(",")[1] and csv[i+8].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+8].split(",")[2])
            elif csv[i+9].split(",")[1] == csv[i].split(",")[1] and csv[i+9].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+9].split(",")[2])
            elif csv[i+10].split(",")[1] == csv[i].split(",")[1] and csv[i+10].split(",")[2].startswith("MSTRG") == False:
                names.append(csv[i+10].split(",")[2])
    
            else:
                names.append(csv[i].split(",")[2])
    
    for i in range(7):
        names.append("Mcrs1\n")
    for i in range(3):
        names.append("MSTRG.19674\n")
    names.append("Gm4366\n")
    print(names[-15:])
    
    #%%
    # Create Other INformation Lists
    sig_list = []
    with open("D:\Data\sig_tissue_results_genes.csv", "r") as csv:
        for line in csv:
            sig_list.append(line.strip().split(","))
    sig_list = sig_list[1:]
    print(sig_list[:5])
    temp_list = []
    with open("get_sig_gene.csv", "r") as csv:
        for line in csv:
            temp_list.append(line)
    temp_list = temp_list[1:]
    
    name_list2 = []
    mstrg_list = []
    for i in temp_list:
        mstrg_list.append(i.split(",")[1])
        name_list2.append(i.strip().split(",")[2])
    #%%
    # Troubleshooting
    print(len(sig_list), len(mstrg_list))
    print((mstrg_list[0]))
    print(sig_list[:10])
    print()
    print(len(names), len(mstrg_list))
    print()
    print(len(sig_list))
    print()
    print(names[mstrg_list.index(sig_list[1][2])])
    print()
    print(mstrg_list.index(sig_list[0][2]))
    print()
    print(names[:15])
    print()
    print(mstrg_list[:15])
    if "Lag3\n" in names:
        print("true")
    with open("D:\Data\get_sig_gene_no_dots.csv", "r") as csv:
        csv = csv.readlines()
        for i in range(10):
            if csv[i].split(",")[2].startswith("MSTRG") == False:
                print("Name")
            else:
                print("MSTRG")
    #%%
    #with open("D:\Data\get_sig_gene_named.csv", "w") as csv:
    #        for i in range(len(sig_list)):
    #            if sig_list[i][2] in mstrg_list:
    #                csv.write(str(sig_list[i][0]) + "," + str(sig_list[i][1]) + "," + str(sig_list[i][2]) + "," + str(sig_list[i][3]) + "," + str(sig_list[i][4]) + "," + str(sig_list[i][5]) + "," + str(names[mstrg_list.index(sig_list[i][2])]))
    #%%
    # Create list to write file from, where gene names are selected based on MSTRG, and if there is a dot the next lines are read and used instead
    name_list2 = names[1:]
    new = sig_list
    for i in range(len(sig_list)):
        if i < len(sig_list) - 10:
            if (sig_list[i][2] in mstrg_list) and (name_list2[mstrg_list.index(sig_list[i][2])] != ".\n"):
                new[i].append(name_list2[mstrg_list.index(sig_list[i][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+1][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+1][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+2][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+2][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+3][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+3][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+4][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+4][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+5][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+5][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+6][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+6][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+7][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+7][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+8][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+8][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+9][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+9][2])])
            elif (sig_list[i][2] in mstrg_list) and mstrg_list[mstrg_list.index(sig_list[i+10][2])] == mstrg_list[mstrg_list.index(sig_list[i][2])]:
                new[i].append(name_list2[mstrg_list.index(sig_list[i+10][2])])
        else:
            if (sig_list[i][2] in mstrg_list):
                new[i].append(name_list2[mstrg_list.index(sig_list[i][2])])
    
    #%% 
    # Troubleshooting
    #print(new[:10])
    #for i in range(len(new)):
    #    for j in new[i]:
    #        if j == "lag3":
    #            print("true")
    #print(len(new[0]))
    #%%
    # Write CSV
    with open("new_ballgown_tissue_sig_genes.csv", "w") as csv:
        for i in new:
            if len(i) == 7:
                csv.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]) + "," + str(i[6]).strip() + "\n")
            else:
                csv.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]) + "," + "\n")
    
            #csv.write(str(i).strip("[") + "\n")
            #csv.write(re.sub("[]))
