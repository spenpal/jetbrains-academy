complement = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}


def complementary_strand(strand):
    return ''.join(complement[base] for base in strand)


def get_plasmid_cut(plasmid, site):
    comp_plasmid = complementary_strand(plasmid)
    site_idx = plasmid.find(site)

    original_cut = [plasmid[:site_idx + 1], plasmid[site_idx + 1:]]
    comp_cut = [comp_plasmid[:site_idx + 5], comp_plasmid[site_idx + 5:]]

    return [original_cut, comp_cut]


def get_gfp_cut(gfp, left_site, right_site):
    comp_gfp = complementary_strand(gfp)
    left_site_idx, right_site_idx = gfp.find(left_site), gfp.rfind(right_site)

    original_cut = gfp[left_site_idx + 1: right_site_idx + 1]
    comp_cut = comp_gfp[left_site_idx + 5: right_site_idx + 5]

    return [original_cut, comp_cut]


def ligation(plasmid_cut, gfp_cut):
    [og_plasmid_left, og_plasmid_right], [comp_plasmid_left, comp_plasmid_right] = plasmid_cut
    og_gfp, comp_gfp = gfp_cut

    print(og_plasmid_left, og_gfp, og_plasmid_right, sep='')
    print(comp_plasmid_left, comp_gfp, comp_plasmid_right, sep='')


# MAIN #
filename = input()
with open(filename) as f:
    plasmid = f.readline().strip()
    plasmid_site = f.readline().strip()
    gfp = f.readline().strip()
    gfp_left_site, gfp_right_site = f.readline().strip().split()

# get cuts
plasmid_cut = get_plasmid_cut(plasmid, plasmid_site)
gfp_cut = get_gfp_cut(gfp, gfp_left_site, gfp_right_site)

# perform ligation and print result
ligation(plasmid_cut, gfp_cut)