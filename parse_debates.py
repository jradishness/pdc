import collections, re
from collections import defaultdict
debate = collections.defaultdict(str)

with open("data/pres_1960_chic.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("THE MODERATOR. "):
                speaker, party = "Mode", "1960M"
                debate[party] += line[15:]
            elif line.startswith("MR. KENNEDY: "):
                speaker, party = "KENNEDY", "1960D"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("MR. NIXON: "):
                speaker, party = "NIXON", "1960R"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1960_nyci.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("THE MODERATOR. "):
                speaker, party = "Mode", "1960M"
                debate[party] += line[15:]
            elif line.startswith("MR. KENNEDY: "):
                speaker, party = "KENNEDY", "1960D"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("MR. NIXON: "):
                speaker, party = "NIXON", "1960R"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1960_nyla.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("THE MODERATOR. "):
                speaker, party = "Mode", "1960M"
                debate[party] += line[15:]
            elif line.startswith("MR. KENNEDY: "):
                speaker, party = "KENNEDY", "1960D"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("MR. NIXON: "):
                speaker, party = "NIXON", "1960R"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1960_wash.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("THE MODERATOR. "):
                speaker, party = "Mode", "1960M"
                debate[party] += line[15:]
            elif line.startswith("MR. KENNEDY: "):
                speaker, party = "KENNEDY", "1960D"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("MR. NIXON: "):
                speaker, party = "NIXON", "1960R"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1976_phil.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("THE MODERATOR. "):
                speaker, party = "Mode", "1976M"
                debate[party] += line[15:]
            elif line.startswith("MR. REYNOLDS. "):
                speaker, party = "Q", "1976M"
                debate[speaker] += line[14:]
                debate[party] += line[14:]
            elif line.startswith("THE PRESIDENT. "):
                speaker = "FORD"
                party = "1976D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.startswith("MR. GANNON. "):
                speaker = "Q"
                party = "1976M"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            elif line.upper().startswith("MS. DREW. "):
                speaker = "Q"
                party = "1976M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.startswith("MR. CARTER. "):
                speaker, party = "CARTER", "1976R"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1976_virg.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("THE MODERATOR. "):
                speaker, party = "Mode", "1976M"
                debate[party] += line[15:]
            elif line.startswith("MR. KRAFT. "):
                speaker, party = "Q", "1976M"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            elif line.startswith("MR. MAYNARD. "):
                speaker, party = "Q", "1976M"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("MR. NELSON. "):
                speaker, party = "Q", "1976M"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            elif line.startswith("THE PRESIDENT. "):
                speaker, party = "FORD", "1976D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.startswith("MR. CARTER. "):
                speaker, party = "CARTER", "1976R"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1976_sanf.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("THE MODERATOR. "):
                speaker, party = "Mode", "1976M"
                debate[party] += line[15:]
            elif line.startswith("MR. FRANKEL. "):
                speaker, party = "Q", "1976M"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("MR. TREWHITT. "):
                speaker, party = "Q", "1976M"
                debate[speaker] += line[14:]
                debate[party] += line[14:]
            elif line.startswith("MR. VALERIANI. "):
                speaker = "Q"
                party = "1976M"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.startswith("THE PRESIDENT. "):
                speaker, party = "FORD", "1976D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.startswith("MR. CARTER. "):
                speaker, party = "CARTER", "1976R"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_1976_hous.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("HOGE: "):
                speaker, party = "Mode", "1976M"
                debate[party] += line[6:]
                debate[speaker] += line[6:]
            elif line.upper().startswith("Q: "):
                speaker, party = "Q", "1976M"
                debate[speaker] += line[3:]
                debate[party] += line[3:]
            elif line.upper().startswith("DOLE: "):
                speaker, party = "DOLE", "1976R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("MONDALE: "):
                speaker, party = "MONDALE", "1976D"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1980_clev.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MR. SMITH. "):
                speaker, party = "Mode", "1980M"
                debate[party] += line[11:]
                debate[speaker] += line[11:]
            elif line.upper().startswith("MRS. HINERFELD. "):
                speaker, party = "Q", "1980M"
                debate[speaker] += line[16:]
                debate[party] += line[16:]
            elif line.upper().startswith("MR. ELLIS. "):
                speaker, party = "Q", "1980M"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            elif line.upper().startswith("MR. HILLIARD. "):
                speaker, party = "Q", "1980M"
                debate[speaker] += line[14:]
                debate[party] += line[14:]
            elif line.upper().startswith("MS. WALTERS. "):
                speaker, party = "Q", "1980M"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.upper().startswith("MR. STONE. "):
                speaker, party = "Q", "1980M"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            elif line.upper().startswith("THE PRESIDENT. "):
                speaker, party = "CARTER", "1980D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.upper().startswith("GOVERNOR REAGAN. "):
                speaker, party = "REAGAN", "1980R"
                debate[speaker] += line[17:]
                debate[party] += line[17:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1984_kcmo.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MS. RIDINGS. "):
                speaker, party = "Mode", "1984M"
                debate[party] += line[13:]
                debate[speaker] += line[13:]
            elif line.upper().startswith("MR. NEWMAN. "):
                speaker, party = "Mode", "1984M"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            elif line.upper().startswith("MS. GEYER. "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            elif line.upper().startswith("MR. KALB. "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.upper().startswith("MR. TREWHITT. "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[14:]
                debate[party] += line[14:]
            elif line.upper().startswith("MR. KONDRACKE. "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.upper().startswith("THE PRESIDENT. "):
                speaker, party = "REAGAN", "1984R"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.upper().startswith("MR. MONDALE. "):
                speaker, party = "MONDALE", "1984D"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1984_kent.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MS. RIDINGS. "):
                speaker, party = "Mode", "1984M"
                debate[party] += line[13:]
                debate[speaker] += line[13:]
            elif line.upper().startswith("MS. WALTERS. "):
                speaker, party = "Mode", "1984M"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.upper().startswith("MR. WIEGHART. "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[14:]
                debate[party] += line[14:]
            elif line.upper().startswith("MS. SAWYER. "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            elif line.upper().startswith("MR. BARNES. "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            elif line.upper().startswith("THE PRESIDENT. "):
                speaker, party = "REAGAN", "1984R"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.upper().startswith("MR. MONDALE. "):
                speaker, party = "MONDALE", "1984D"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_1984_phil.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("RIDINGS: "):
                speaker, party = "Mode", "1984M"
                debate[party] += line[9:]
                debate[speaker] += line[9:]
            elif line.upper().startswith("VANOCUR: "):
                speaker, party = "Mode", "1984M"
                debate[party] += line[9:]
                debate[speaker] += line[9:]
            elif line.upper().startswith("BOYD: "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("MASHEK: "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("WHITE: "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            elif line.upper().startswith("QUARLES: "):
                speaker, party = "Q", "1984M"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            elif line.upper().startswith("BUSH: "):
                speaker, party = "BUSH_41", "1984R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("FERRARO: "):
                speaker, party = "FERRARO", "1984D"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1988_ucla.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("SHAW: "):
                speaker, party = "Mode", "1988M"
                debate[party] += line[6:]
                debate[speaker] += line[6:]
            elif line.upper().startswith("COMPTON: "):
                speaker, party = "Mode", "1988M"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            elif line.upper().startswith("WARNER: "):
                speaker, party = "Mode", "1988M"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("MITCHELL: "):
                speaker, party = "Mode", "1988M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.upper().startswith("BUSH: "):
                speaker, party = "BUSH_41", "1988R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("DUKAKIS: "):
                speaker, party = "DUKAKIS", "1988D"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1988_wsnc.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("LEHRER: "):
                speaker, party = "Mode", "1988M"
                debate[party] += line[8:]
                debate[speaker] += line[8:]
            elif line.upper().startswith("MASHEK: "):
                speaker, party = "Mode", "1988M"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("GROER: "):
                speaker, party = "Mode", "1988M"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            elif line.upper().startswith("JENNINGS: "):
                speaker, party = "Mode", "1988M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.upper().startswith("BUSH: "):
                speaker, party = "BUSH_41", "1988R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("DUKAKIS: "):
                speaker, party = "DUKAKIS", "1988D"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_1988_nebr.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("WOODRUFF: "):
                speaker, party = "Mode", "1988M"
                debate[party] += line[10:]
                debate[speaker] += line[10:]
            elif line.upper().startswith("MARGOLIS: "):
                speaker, party = "Mode", "1988M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.upper().startswith("BROKAW: "):
                speaker, party = "Mode", "1988M"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("HUME: "):
                speaker, party = "Mode", "1988M"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("QUAYLE: "):
                speaker, party = "QUAYLE", "1988R"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("BENTSEN: "):
                speaker, party = "BENTSEN", "1988D"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1992_mich.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MR. LEHRER. "):
                speaker, party = "Mode", "1992M"
                debate[party] += line[12:]
                debate[speaker] += line[12:]
            elif line.upper().startswith("MS. ROOK. "):
                speaker, party = "Q", "1992M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.upper().startswith("PRESIDENT BUSH. "):
                speaker, party = "BUSH_41", "1992R"
                debate[speaker] += line[16:]
                debate[party] += line[16:]
            elif line.upper().startswith("GOVERNOR CLINTON. "):
                speaker, party = "CLINTON_W", "1992D"
                debate[speaker] += line[18:]
                debate[party] += line[18:]
            elif line.upper().startswith("MR. PEROT. "):
                speaker, party = "PEROT", "1992I"
                debate[speaker] += line[18:]
                debate[party] += line[18:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1992_stlo.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MR. LEHRER. "):
                speaker, party = "Mode", "1992M"
                debate[party] += line[12:]
                debate[speaker] += line[12:]
            elif line.upper().startswith("MS. ROOK. "):
                speaker, party = "Q", "1992M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.upper().startswith("ANN COMPTON. ") or line.upper().startswith("MS. COMPTON. "):
                speaker, party = "Q", "1992M"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.upper().startswith("SANDER VANOCUR. "):
                speaker, party = "Q", "1992M"
                debate[speaker] += line[16:]
                debate[party] += line[16:]
            elif line.upper().startswith("MR. MASHEK. "):
                speaker, party = "Q", "1992M"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            elif line.upper().startswith("MR. VANOCUR. "):
                speaker, party = "Q", "1992M"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.upper().startswith("MR. GIBBONS. "):
                speaker, party = "Q", "1992M"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.upper().startswith("PRESIDENT BUSH. "):
                speaker, party = "BUSH_41", "1992R"
                debate[speaker] += line[16:]
                debate[party] += line[16:]
            elif line.upper().startswith("GOVERNOR CLINTON. "):
                speaker, party = "CLINTON_W", "1992D"
                debate[speaker] += line[18:]
                debate[party] += line[18:]
            elif line.upper().startswith("MR. PEROT. "):
                speaker, party = "PEROT", "1992I"
                debate[speaker] += line[18:]
                debate[party] += line[18:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1992_virg.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MS. SIMPSON. "):
                speaker, party = "Mode", "1992M"
                debate[party] += line[13:]
                debate[speaker] += line[13:]
            elif line.upper().startswith("Q. "):
                speaker, party = "Q", "1992M"
                debate[speaker] += line[3:]
                debate[party] += line[3:]
            elif line.upper().startswith("PRESIDENT BUSH. "):
                speaker, party = "BUSH_41", "1992R"
                debate[speaker] += line[16:]
                debate[party] += line[16:]
            elif line.upper().startswith("GOVERNOR CLINTON. "):
                speaker, party = "CLINTON_W", "1992D"
                debate[speaker] += line[18:]
                debate[party] += line[18:]
            elif line.upper().startswith("MR. PEROT. "):
                speaker, party = "PEROT", "1992I"
                debate[speaker] += line[18:]
                debate[party] += line[18:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_1992_atla.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("BRUNO: "):
                speaker, party = "Mode", "1992M"
                debate[party] += line[7:]
                debate[speaker] += line[7:]
            elif line.upper().startswith("QUAYLE: "):
                speaker, party = "QUAYLE", "1992R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("GORE: "):
                speaker, party = "GORE", "1992D"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("STOCKDALE: "):
                speaker, party = "STOCKDALE", "1992I"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1996_hart.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MR. LEHRER. "):
                speaker, party = "Mode", "1996M"
                debate[party] += line[12:]
                debate[speaker] += line[12:]
            elif line.upper().startswith("SENATOR DOLE. "):
                speaker, party = "DOLE", "1996R"
                debate[speaker] += line[14:]
                debate[party] += line[14:]
            elif line.upper().startswith("THE PRESIDENT. "):
                speaker, party = "CLINTON_W", "1996D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_1996_sdca.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MR. LEHRER. "):
                speaker, party = "Mode", "1996M"
                debate[party] += line[12:]
                debate[speaker] += line[12:]
            elif line.upper().startswith("Q. "):
                speaker, party = "Q", "1996M"
                debate[speaker] += line[3:]
                debate[party] += line[3:]
            elif line.upper().startswith("SENATOR DOLE. "):
                speaker, party = "DOLE", "1996R"
                debate[speaker] += line[14:]
                debate[party] += line[14:]
            elif line.upper().startswith("THE PRESIDENT. "):
                speaker, party = "CLINTON_W", "1996D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_1996_stpe.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("LEHRER: "):
                speaker, party = "Mode", "1996M"
                debate[party] += line[8:]
                debate[speaker] += line[8:]
            elif line.upper().startswith("KEMP: "):
                speaker, party = "KEMP", "1996R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("GORE: "):
                speaker, party = "GORE", "1996D"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2000_bost.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MODERATOR: "):
                speaker, party = "Mode", "2000M"
                debate[party] += line[11:]
                debate[speaker] += line[11:]
            elif line.upper().startswith("BUSH: "):
                speaker, party = "BUSH_43", "2000R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("GORE: "):
                speaker, party = "GORE", "2000D"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2000_stlo.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MODERATOR: "):
                speaker, party = "Mode", "2000M"
                debate[party] += line[11:]
                debate[speaker] += line[11:]
            elif line.upper().startswith("MEMBER OF AUDIENCE: "):
                speaker, party = "Q", "2000M"
                debate[speaker] += line[20:]
                debate[party] += line[20:]
            elif line.upper().startswith("BUSH: "):
                speaker, party = "BUSH_43", "2000R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("GORE: "):
                speaker, party = "GORE", "2000D"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2000_wsnc.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MODERATOR: "):
                speaker, party = "Mode", "2000M"
                debate[party] += line[11:]
                debate[speaker] += line[11:]
            elif line.upper().startswith("BUSH: "):
                speaker, party = "BUSH_43", "2000R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("GORE: "):
                speaker, party = "GORE", "2000D"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_2000_kent.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MODERATOR: "):
                speaker, party = "Mode", "2000M"
                debate[party] += line[11:]
                debate[speaker] += line[11:]
            elif line.upper().startswith("CHENEY: "):
                speaker, party = "CHENEY", "2000R"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("LIEBERMAN: "):
                speaker, party = "LIEBERMAN", "2000D"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2004_ariz.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MR. SCHIEFFER. "):
                speaker, party = "Mode", "2004M"
                debate[party] += line[15:]
                debate[speaker] += line[15:]
            elif line.upper().startswith("PRESIDENT BUSH. "):
                speaker, party = "BUSH_43", "2004R"
                debate[speaker] += line[16:]
                debate[party] += line[16:]
            elif line.upper().startswith("SENATOR KERRY. "):
                speaker, party = "GORE", "2004D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2004_flor.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MR. LEHRER. "):
                speaker, party = "Mode", "2004M"
                debate[party] += line[12:]
                debate[speaker] += line[12:]
            elif line.upper().startswith("PRESIDENT BUSH. "):
                speaker, party = "BUSH_43", "2004R"
                debate[speaker] += line[16:]
                debate[party] += line[16:]
            elif line.upper().startswith("SENATOR KERRY. "):
                speaker, party = "GORE", "2004D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2004_stmo.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("MR. GIBSON. "):
                speaker, party = "Mode", "2004M"
                debate[party] += line[12:]
                debate[speaker] += line[12:]
            elif line.upper().startswith("Q. "):
                speaker, party = "Q", "2004M"
                debate[speaker] += line[3:]
                debate[party] += line[3:]
            elif line.upper().startswith("MR. DAHLE. ") or \
                    line.upper().startswith("MR. BALDI. "):
                speaker, party = "Q", "2004M"
                debate[speaker] += line[11:]
                debate[party] += line[11:]
            elif line.upper().startswith("CHERYL OTIS. "):
                speaker, party = "Q", "2004M"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.upper().startswith("DANIEL FARLEY. ") or \
                    line.upper().startswith("RANDEE JACOBS. ") or \
                    line.upper().startswith("JOHN HORSTMAN. "):
                speaker, party = "Q", "2004M"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.upper().startswith("NIKKI WASHINGTON. "):
                speaker, party = "Q", "2004M"
                debate[speaker] += line[18:]
                debate[party] += line[18:]
            elif line.upper().startswith("ANN BRONSING. "):
                speaker, party = "Q", "2004M"
                debate[speaker] += line[14:]
                debate[party] += line[14:]
            elif line.upper().startswith("PRESIDENT BUSH. "):
                speaker, party = "BUSH_43", "2004R"
                debate[speaker] += line[16:]
                debate[party] += line[16:]
            elif line.upper().startswith("SENATOR KERRY. "):
                speaker, party = "KERRY", "2004D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_2004_clev.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("IFILL: "):
                speaker, party = "Mode", "2004M"
                debate[party] += line[7:]
                debate[speaker] += line[7:]
            elif line.upper().startswith("CHENEY: "):
                speaker, party = "CHENEY", "2004R"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("EDWARDS: "):
                speaker, party = "EDWARDS", "2004D"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2008_hemp.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("SCHIEFFER: "):
                speaker, party = "Mode", "2008M"
                debate[party] += line[11:]
                debate[speaker] += line[11:]
            elif line.upper().startswith("MCCAIN: "):
                speaker, party = "MCCAIN", "2008R"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("OBAMA: "):
                speaker, party = "OBAMA", "2008D"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2008_nash.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("BROKAW: "):
                speaker, party = "Mode", "2008M"
                debate[party] += line[8:]
                debate[speaker] += line[8:]
            elif line.upper().startswith("QUESTION: "):
                speaker, party = "Q", "2008M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.upper().startswith("MCCAIN: "):
                speaker, party = "MCCAIN", "2008R"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("OBAMA: "):
                speaker, party = "OBAMA", "2008D"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2008_oxms.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("LEHRER: "):
                speaker, party = "Mode", "2008M"
                debate[party] += line[8:]
                debate[speaker] += line[8:]
            elif line.upper().startswith("MCCAIN: "):
                speaker, party = "MCCAIN", "2008R"
                debate[speaker] += line[8:]
                debate[party] += line[8:]
            elif line.upper().startswith("OBAMA: "):
                speaker, party = "OBAMA", "2008D"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_2008_stmo.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("IFILL: "):
                speaker, party = "Mode", "2008M"
                debate[party] += line[7:]
                debate[speaker] += line[7:]
            elif line.upper().startswith("PALIN: "):
                speaker, party = "PALIN", "2008R"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            elif line.upper().startswith("BIDEN: "):
                speaker, party = "BIDEN", "2008D"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2012_denv.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("Mr. Lehrer. "):
                speaker, party = "Mode", "2012M"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            elif line.startswith("The President. "):
                speaker = "OBAMA"
                party = "2012D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.startswith("Gov. Romney. "):
                speaker = "ROMNEY"
                party = "2012R"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("Mr. Romney. "):
                speaker = "ROMNEY"
                party = "2012R"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2012_hemp.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("Ms. Crowley. "):
                speaker, party = "Mode", "2012M"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("Q. "):
                speaker, party = "Q", "2012M"
                debate[speaker] += line[3:]
                debate[party] += line[3:]
            elif line.startswith("The President. "):
                speaker = "OBAMA"
                party = "2012D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.startswith("Gov. Romney. "):
                speaker = "ROMNEY"
                party = "2012R"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("Mr. Romney. "):
                speaker = "ROMNEY"
                party = "2012R"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2012_flor.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.startswith("Mr. Schieffer. "):
                speaker, party = "Mode", "2012M"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif re.search(r'[a-z]/[A-Z]', line):
                speaker, party = "Mode", "2012M"
                debate[speaker] += line
                debate[party] += line
            elif line.startswith("Q. "):
                speaker, party = "Q", "2012M"
                debate[speaker] += line[3:]
                debate[party] += line[3:]
            elif line.startswith("The President. "):
                speaker = "OBAMA"
                party = "2012D"
                debate[speaker] += line[15:]
                debate[party] += line[15:]
            elif line.startswith("Gov. Romney. "):
                speaker = "ROMNEY"
                party = "2012R"
                debate[speaker] += line[13:]
                debate[party] += line[13:]
            elif line.startswith("Mr. Romney. "):
                speaker = "ROMNEY"
                party = "2012R"
                debate[speaker] += line[12:]
                debate[party] += line[12:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_2012_kent.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("RADDATZ: "):
                speaker, party = "Mode", "2012M"
                debate[party] += line[9:]
                debate[speaker] += line[9:]
            elif line.upper().startswith("RYAN: "):
                speaker, party = "RYAN", "2012R"
                debate[speaker] += line[6:]
                debate[party] += line[6:]
            elif line.upper().startswith("BIDEN: "):
                speaker, party = "BIDEN", "2012D"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2016_hemp.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("HOLT: "):
                speaker, party = "Mode", "2016M"
                debate[party] += line[6:]
                debate[speaker] += line[6:]
            elif line.upper().startswith("TRUMP: "):
                speaker, party = "TRUMP", "2016R"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            elif line.upper().startswith("CLINTON: "):
                speaker, party = "CLINTON_H", "2016D"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2016_stmo.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("RADDATZ: "):
                speaker, party = "Mode", "2016M"
                debate[party] += line[9:]
                debate[speaker] += line[9:]
            elif line.upper().startswith("COOPER: "):
                speaker, party = "Mode", "2016M"
                debate[party] += line[8:]
                debate[speaker] += line[8:]
            elif line.upper().startswith("QUESTION: "):
                speaker, party = "Q", "2016M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.upper().startswith("TRUMP: "):
                speaker, party = "TRUMP", "2016R"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            elif line.upper().startswith("CLINTON: "):
                speaker, party = "CLINTON_H", "2016D"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/pres_2016_unlv.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("WALLACE: "):
                speaker, party = "Mode", "2016M"
                debate[party] += line[9:]
                debate[speaker] += line[9:]
            elif line.upper().startswith("QUESTION: "):
                speaker, party = "Q", "2016M"
                debate[speaker] += line[10:]
                debate[party] += line[10:]
            elif line.upper().startswith("TRUMP: "):
                speaker, party = "TRUMP", "2016R"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            elif line.upper().startswith("CLINTON: "):
                speaker, party = "CLINTON_H", "2016D"
                debate[speaker] += line[9:]
                debate[party] += line[9:]
            else:
                debate[speaker] += line
                debate[party] += line

with open("data/veep_2016_virg.txt", 'r') as f:
    speaker, party = "META", ""
    for line in f:
        if len(line) == 0:
            pass
        else:
            if line.upper().startswith("QUIJANO: "):
                speaker, party = "Mode", "2016M"
                debate[party] += line[9:]
                debate[speaker] += line[9:]
            elif line.upper().startswith("PENCE: "):
                speaker, party = "PENCE", "2016R"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            elif line.upper().startswith("KAINE: "):
                speaker, party = "KAINE", "2016D"
                debate[speaker] += line[7:]
                debate[party] += line[7:]
            else:
                debate[speaker] += line
                debate[party] += line

for x in debate:
    with open('results/' + str(x) + '.txt', 'w') as f:
        print(debate[x], file=f)
