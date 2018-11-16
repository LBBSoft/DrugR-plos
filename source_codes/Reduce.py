def drug_ins():
    dtype=root.attrib['type']
    created=root.attrib['created']
    updated=root.attrib['updated']
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    did=root[inx].text
    inx=0
    while (root[inx].tag !='name'):
        inx=inx+1
        if inx>=len(root):
            break
    dname=""
    if inx<len(root):
        dname=root[inx].text
    inx=0
    while (root[inx].tag !='description'):
        inx=inx+1
        if inx>=len(root):
            break
    description=""
    if inx<len(root):
        description=root[inx].text
    inx=0
    while (root[inx].tag !='cas-number'):
        inx=inx+1
        if inx>=len(root):
            break
    casenumber=""
    if inx<len(root):
        casenumber=root[inx].text
    inx=0
    while (root[inx].tag !='unii'):
        inx=inx+1
        if inx>=len(root):
            break
    unii=""
    if inx<len(root):
        unii=root[inx].text
    inx=0
    while (root[inx].tag !='state'):
        inx=inx+1
        if inx>=len(root):
            break
    state=""
    if inx<len(root):
        state=root[inx].text
    qry = "set nocount off set ansi_warnings off insert into  drugs select '"+dtype+"','"+created+"','"+updated+"','"+did+"','"+dname+"','"+description+"','"+(casenumber)+"','"+unii+"','"+state+"' where not exists(select id from drugs where id='"+did+"')"
    cur.execute(qry)
    con.commit()

def drug_second_id_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='drugbank-id':
            if 'primary' not in root[x].attrib:
                second_id=root[x].text
                qry = "set nocount off set ansi_warnings off insert into  drug_second_id select '"+primary_id+"','"+second_id+"' where not exists(select id from drug_second_id where id='"+primary_id+"' and second_id='"+second_id+"')"
                cur.execute(qry)
                con.commit()

def drug_groups_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='groups':
            for j in range(0,len(root[x])):
                grp=root[x][j].text
                qry = "set nocount off set ansi_warnings off insert into  drug_groups select '"+primary_id+"','"+grp+"' where not exists(select id from drug_groups where id='"+primary_id+"' and groups='"+grp+"')"
                cur.execute(qry)
                con.commit()

def drug_reference_article_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='general-references':
            for j in range(0,len(root[x])):
                if root[x][j].tag=='articles':
                    for i in range(0,len(root[x][j])):
                        pub_id=root[x][j][i][0].text
                        cite=root[x][j][i][1].text
                        grp=root[x][j].text
                        qry = "set nocount off set ansi_warnings off insert into  drug_reference_articles select '"+primary_id+"','"+pub_id+"','"+cite+"' where not exists(select drug_id from drug_reference_articles where drug_id='"+primary_id+"' and pubmed_id='"+pub_id+"')"
                        cur.execute(qry)
                        con.commit()

def drug_reference_text_book_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='general-references':
            for j in range(0,len(root[x])):
                if root[x][j].tag=='textbooks':
                    for i in range(0,len(root[x][j])):
                        isbn=root[x][j][i][0].text
                        cite=root[x][j][i][1].text
                        grp=root[x][j].text
                        qry = "set nocount off set ansi_warnings off insert into  drug_reference_books select '"+primary_id+"','"+str(i+1)+"','"+isbn+"','"+cite+"' where not exists(select drug_id from drug_reference_books where drug_id='"+primary_id+"' and isbn='"+isbn+"' and counter='"+str(i+1)+"')"
                        cur.execute(qry)
                        con.commit()

def drug_reference_text_link_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='general-references':
            for j in range(0,len(root[x])):
                if root[x][j].tag=='links':
                    for i in range(0,len(root[x][j])):
                        title=root[x][j][i][0].text
                        link=root[x][j][i][1].text
                        grp=root[x][j].text
                        qry = "set nocount off set ansi_warnings off insert into  drug_reference_link select '"+primary_id+"','"+str(i+1)+"','"+title+"','"+link+"' where not exists(select drug_id from drug_reference_link where drug_id='"+primary_id+"' and counter='"+str(i+1)+"')"
                        cur.execute(qry)
                        con.commit()

def drugs_properties_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    inx=0
    synth="unknown"
    while (root[inx].tag!='synthesis-reference'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        synth=root[inx].text
    inx=0
    indication="unknown"
    while (root[inx].tag!='indication'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        indication=root[inx].text
    inx=0
    phar="unknown"
    while (root[inx].tag!='pharmacodynamics'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        phar=root[inx].text
    inx=0
    mechanism="unknown"
    while (root[inx].tag!='mechanism-of-action'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        mechanism=root[inx].text
    inx=0
    toxicity="unknown"
    while (root[inx].tag!='toxicity'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        toxicity=root[inx].text
    inx=0
    metabolism="unknown"
    while (root[inx].tag!='metabolism'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        metabolism=root[inx].text
    inx=0
    absorption="unknown"
    while (root[inx].tag!='absorption'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        absorption=root[inx].text
    inx=0
    half_life="unknown"
    while (root[inx].tag!='half-life'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        half_life=root[inx].text
    inx=0
    p_bind="unknown"
    while (root[inx].tag!='protein-binding'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        p_bind=root[inx].text
    inx=0
    r_o_elimination="unknown"
    while (root[inx].tag!='route-of-elimination'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        r_o_elimination=root[inx].text
    inx=0
    v_o_distribution="unknown"
    while (root[inx].tag!='volume-of-distribution'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        v_o_distribution=root[inx].text
    inx=0
    clearance="unknown"
    while (root[inx].tag!='clearance'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        clearance=root[inx].text
    inx=0
    fda_label="unknown"
    while (root[inx].tag!='fda-label'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        fda_label=root[inx].text
    inx=0
    msds="unknown"
    while (root[inx].tag!='msds'):
        inx=inx+1
        if inx>=len(root):
            break
    if inx<len(root):
        msds=root[inx].text
    qry = "set nocount off set ansi_warnings off insert into  drug_properties select '"+primary_id+"','"+synth+"','"+indication+"','"+phar+"','"+mechanism+"','"+toxicity+"','"+metabolism+"','"+absorption+"','"+half_life+"','"+p_bind+"','"+r_o_elimination+"','"+v_o_distribution+"','"+clearance+"','"+fda_label+"','"+msds+"' where not exists(select id from drug_properties where id='"+primary_id+"')"
    cur.execute(qry)
    con.commit()

def drug_classification_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='classification':
            description=root[x][0].text
            directparent=root[x][1].text
            kingdom=root[x][2].text
            superclass=root[x][3].text
            mainclass=root[x][4].text
            subclass=root[x][5].text
            qry = "set nocount off set ansi_warnings off insert into  drug_classification select '"+primary_id+"','"+description+"','"+directparent+"','"+kingdom+"','"+superclass+"','"+mainclass+"','"+subclass+"' where not exists(select drug_id from drug_classification where drug_id='"+primary_id+"' and classification_description='"+description+"')"
            cur.execute(qry)
            con.commit()
            for j in range(0,len(root[x])):
                if root[x][j].tag=="alternative-parent":
                    alternative_parent=root[x][j].text
                    qry = "set nocount off set ansi_warnings off insert into  drug_classification_alternative_parent select '"+primary_id+"','"+str(j+1)+"','"+description+"','"+alternative_parent+"' where not exists(select drug_id from drug_classification_alternative_parent where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                    cur.execute(qry)
                    con.commit()
            for j in range(0,len(root[x])):
                if root[x][j].tag=="substituent":
                    substituent=root[x][j].text
                    qry = "set nocount off set ansi_warnings off insert into  drug_classification_substituent select '"+primary_id+"','"+str(j+1)+"','"+description+"','"+substituent+"' where not exists(select drug_id from drug_classification_substituent where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                    cur.execute(qry)
                    con.commit()

def drug_salt_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='salts':
            for j in range(0,len(root[x])):
                salt_id=root[x][j][0].text
                salt_name=root[x][j][1].text
                unii=root[x][j][2].text
                case_number=root[x][j][3].text
                inchikey=root[x][j][4].text
                qry = "set nocount off set ansi_warnings off insert into  drug_salt select '"+primary_id+"','"+salt_id+"','"+salt_name+"','"+unii+"','"+case_number+"','"+inchikey+"' where not exists(select drug_id from drug_salt where drug_id='"+primary_id+"' and drug_salt_id='"+salt_id+"')"
                cur.execute(qry)
                con.commit()

def drug_synonyms_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='synonyms':
            for j in range(0,len(root[x])):
                language=root[x][j].attrib['language']
                coder=root[x][j].attrib['coder']
                description=root[x][j].text
                qry = "set nocount off set ansi_warnings off insert into  drug_synonyms select '"+primary_id+"','"+str(j+1)+"','"+language+"','"+coder+"','"+description+"' where not exists(select drug_id from drug_synonyms where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_product_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='products':
            for j in range(0,len(root[x])):
                pname=root[x][j][0].text
                labeller=root[x][j][1].text
                ndcid=root[x][j][2].text
                ndc_product_code=root[x][j][3].text
                dpd_id=root[x][j][4].text
                s_date=root[x][j][5].text
                e_date=root[x][j][6].text
                dosage=root[x][j][7].text
                strength=root[x][j][8].text
                product_route=root[x][j][9].text
                fda_number=root[x][j][10].text
                generic=root[x][j][11].text
                over_counter=root[x][j][12].text
                approved=root[x][j][13].text
                country=root[x][j][14].text
                product_source=root[x][j][15].text
                qry = "set nocount off set ansi_warnings off insert into  drug_products select '"+primary_id+"','"+str(j+1)+"','"+pname+"','"+labeller+"','"+ndcid+"','"+ndc_product_code+"','"+dpd_id+"','"+s_date+"','"+e_date+"','"+dosage+"','"+strength+"','"+product_route+"','"+fda_number+"','"+generic+"','"+over_counter+"','"+approved+"','"+country+"','"+product_source+"' where not exists(select drug_id from drug_products where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_brand_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='international-brands':
            for j in range(0,len(root[x])):
                brand_name=root[x][j][0].text
                company=root[x][j][1].text
                qry = "set nocount off set ansi_warnings off insert into  drug_international_brand select '"+primary_id+"','"+str(j+1)+"','"+brand_name+"','"+company+"' where not exists(select drug_id from drug_international_brand where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_mixture_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='mixtures':
            for j in range(0,len(root[x])):
                mixture_name=root[x][j][0].text
                ingredients=root[x][j][1].text
                qry = "set nocount off set ansi_warnings off insert into  drug_mixture select '"+primary_id+"','"+str(j+1)+"','"+mixture_name+"','"+ingredients+"' where not exists(select drug_id from drug_mixture where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_packager_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='packagers':
            for j in range(0,len(root[x])):
                packager_name=root[x][j][0].text
                url=root[x][j][1].text
                qry = "set nocount off set ansi_warnings off insert into  drug_packagers select '"+primary_id+"','"+packager_name+"','"+url+"' where not exists(select drug_id from drug_packagers where drug_id='"+primary_id+"' and packager_name='"+packager_name+"')"
                cur.execute(qry)
                con.commit()

def drug_manufactors_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='manufacturers':
            for j in range(0,len(root[x])):
                manufactor_name=root[x][j].text
                generic=''
                if 'generic' in (root[x][j].attrib):
                    generic=root[x][j].attrib['generic']
                url=''
                if 'url' in (root[x][j].attrib):
                    url=root[x][j].attrib['url']
                qry = "set nocount off set ansi_warnings off insert into  drug_manufactor select '"+primary_id+"','"+generic+"','"+url+"','"+manufactor_name+"' where not exists(select drug_id from drug_manufactor where drug_id='"+primary_id+"' and manufactor='"+manufactor_name+"')"
                cur.execute(qry)
                con.commit()

def drug_price_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='prices':
            for j in range(0,len(root[x])):
                description=root[x][j][0].text
                cost=root[x][j][1].text
                unit=root[x][j][2].text
                currency=root[x][j][1].attrib['currency'];
                qry = "set nocount off set ansi_warnings off insert into  drug_price select '"+primary_id+"','"+str(j+1)+"','"+description+"','"+currency+"','"+cost+"','"+unit+"' where not exists(select drug_id from drug_price where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_category_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='categories':
            for j in range(0,len(root[x])):
                category=root[x][j][0].text
                mesh_id=root[x][j][1].text
                qry = "set nocount off set ansi_warnings off insert into  drug_category select '"+primary_id+"','"+category+"','"+mesh_id+"' where not exists(select drug_id from drug_category where drug_id='"+primary_id+"' and category='"+category+"')"
                cur.execute(qry)
                con.commit()

def drug_affected_organism_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='affected-organisms':
            for j in range(0,len(root[x])):
                organism=root[x][j].text
                qry = "set nocount off set ansi_warnings off insert into  drug_affected_organism select '"+primary_id+"','"+organism+"' where not exists(select drug_id from drug_affected_organism where drug_id='"+primary_id+"' and organism='"+organism+"')"
                cur.execute(qry)
                con.commit()

def drug_dosage_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='dosages':
            for j in range(0,len(root[x])):
                form=root[x][j][0].text
                dosage_route=root[x][j][1].text
                strength=root[x][j][2].text
                qry = "set nocount off set ansi_warnings off insert into  drug_dosage select '"+primary_id+"','"+str(j+1)+"','"+form+"','"+dosage_route+"','"+strength+"' where not exists(select drug_id from drug_dosage where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_atc_code_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='atc-codes':
            for j in range(0,len(root[x])):
                atc_code=root[x][j].attrib['code']
                qry = "set nocount off set ansi_warnings off insert into  drug_atc_codes select '"+primary_id+"','"+atc_code+"' where not exists(select drug_id from drug_atc_codes where drug_id='"+primary_id+"' and atc_code='"+atc_code+"')"
                cur.execute(qry)
                con.commit()
                for i in range(0,len(root[x][j])):
                    level_code=root[x][j][i].attrib['code']
                    level_description=root[x][j][i].text
                    qry = "set nocount off set ansi_warnings off insert into  atc_codes select '"+primary_id+"','"+atc_code+"','"+level_code+"','"+level_description+"' where not exists(select drug_id from atc_codes where drug_id='"+primary_id+"' and level_code='"+level_code+"' and atc_code='"+atc_code+"')"
                    cur.execute(qry)
                    con.commit()

def drug_ahfs_code_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='ahfs-codes':
            for j in range(0,len(root[x])):
                ahf_code=root[x][j].text
                qry = "set nocount off set ansi_warnings off insert into  drug_ahf_codes select '"+primary_id+"','"+ahf_code+"' where not exists(select drug_id from drug_ahf_codes where drug_id='"+primary_id+"' and ahf_code='"+ahf_code+"')"
                cur.execute(qry)
                con.commit()

def drug_pdb_entries_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='pdb-entries':
            for j in range(0,len(root[x])):
                entry=root[x][j].text
                qry = "set nocount off set ansi_warnings off insert into  drug_pdb_entries select '"+primary_id+"','"+entry+"' where not exists(select drug_id from drug_pdb_entries where drug_id='"+primary_id+"' and pdb_entry='"+entry+"')"
                cur.execute(qry)
                con.commit()

def drug_patent_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='patents':
            for j in range(0,len(root[x])):
                num=root[x][j][0].text
                country=root[x][j][1].text
                approved=root[x][j][2].text
                expire=root[x][j][3].text
                pediatric=root[x][j][4].text
                qry = "set nocount off set ansi_warnings off insert into  drug_patent select '"+primary_id+"','"+num+"','"+country+"','"+approved+"','"+expire+"','"+pediatric+"' where not exists(select drug_id from drug_patent where drug_id='"+primary_id+"' and patent_number='"+num+"')"
                cur.execute(qry)
                con.commit()

def drug_food_interaction_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='food-interactions':
            for j in range(0,len(root[x])):
                interaction=root[x][j].text
                qry = "set nocount off set ansi_warnings off insert into  drug_food_interaction select '"+primary_id+"','"+interaction+"' where not exists(select drug_id from drug_food_interaction where drug_id='"+primary_id+"' and interaction='"+interaction+"')"
                cur.execute(qry)
                con.commit()

def drug_interaction_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='drug-interactions':
            for j in range(0,len(root[x])):
                drug_id=root[x][j][0].text
                drug_name=root[x][j][1].text
                description=root[x][j][2].text
                qry = "set nocount off set ansi_warnings off insert into  drug_interactions select '"+primary_id+"','"+drug_id+"','"+str(j+1)+"','"+drug_name+"','"+description+"' where not exists(select drug_id from drug_interactions where drug_id='"+primary_id+"' and interaction_id='"+drug_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_sequence_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='sequences':
            for j in range(0,len(root[x])):
                seq_format=root[x][j].attrib['format']
                seq=root[x][j].text
                qry = "set nocount off set ansi_warnings off insert into  drug_sequence select '"+primary_id+"','"+str(j+1)+"','"+seq_format+"','"+seq+"' where not exists(select drug_id from drug_sequence where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_experimental_properties_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='experimental-properties':
            for j in range(0,len(root[x])):
                kind=root[x][j][0].text
                value=root[x][j][1].text
                src=root[x][j][2].text
                qry = "set nocount off set ansi_warnings off insert into  drug_experimental_properties select '"+primary_id+"','"+str(j+1)+"','"+kind+"','"+value+"','"+src+"' where not exists(select drug_id from drug_experimental_properties where drug_id='"+primary_id+"' and kind='"+kind+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_calculated_properties_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='calculated-properties':
            for j in range(0,len(root[x])):
                kind=root[x][j][0].text
                value=root[x][j][1].text
                src=root[x][j][2].text
                qry = "set nocount off set ansi_warnings off insert into  drug_calculated_properties select '"+primary_id+"','"+str(j+1)+"','"+kind+"','"+value+"','"+src+"' where not exists(select drug_id from drug_calculated_properties where drug_id='"+primary_id+"' and kind='"+kind+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_external_identifiers_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='external-identifiers':
            for j in range(0,len(root[x])):
                rsc=root[x][j][0].text
                identifier=root[x][j][1].text
                qry = "set nocount off set ansi_warnings off insert into  drug_external_identifiers select '"+primary_id+"','"+str(j+1)+"','"+rsc+"','"+identifier+"' where not exists(select drug_id from drug_external_identifiers where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_external_links_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='external-links':
            for j in range(0,len(root[x])):
                rsc=root[x][j][0].text
                url=root[x][j][1].text
                qry = "set nocount off set ansi_warnings off insert into  drug_external_links select '"+primary_id+"','"+rsc+"','"+url+"' where not exists(select drug_id from drug_external_links where drug_id='"+primary_id+"' and link_resource='"+rsc+"')"
                cur.execute(qry)
                con.commit()

def drug_pathways_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='pathways':
            for j in range(0,len(root[x])):
                inx=0
                while root[x][j][inx].tag!='smpdb-id':
                    inx=inx+1;
                smpdb_id=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='name':
                    inx=inx+1;
                pathway_name=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='category':
                    inx=inx+1;
                category=root[x][j][inx].text
                qry = "set nocount off set ansi_warnings off insert into  drug_pathways select '"+primary_id+"','"+smpdb_id+"','"+pathway_name+"','"+category+"' where not exists(select drug_id from drug_pathways where drug_id='"+primary_id+"' and smpdb_id='"+smpdb_id+"')"
                cur.execute(qry)
                con.commit()
                inx=0
                while root[x][j][inx].tag!='drugs':
                    inx=inx+1;
                for i in range(0,len(root[x][j][inx])):
                    drug_id=root[x][j][inx][i][0].text
                    qry = "set nocount off set ansi_warnings off insert into  drug_pathway_drug select '"+primary_id+"','"+smpdb_id+"','"+drug_id+"' where not exists(select drug_id from drug_pathway_drug where drug_id='"+primary_id+"' and smpdb_id='"+smpdb_id+"' and second_drug_id='"+drug_id+"')"
                    cur.execute(qry)
                    con.commit()
                inx=0
                while root[x][j][inx].tag!='enzymes':
                    inx=inx+1;
                for i in range(0,len(root[x][j][inx])):
                    uniprot_id=root[x][j][inx][i].text
                    qry = "set nocount off set ansi_warnings off insert into  drug_pathway_enzymes select '"+primary_id+"','"+smpdb_id+"','"+uniprot_id+"' where not exists(select drug_id from drug_pathway_enzymes where drug_id='"+primary_id+"' and smpdb_id='"+smpdb_id+"' and uniprot_id='"+uniprot_id+"')"
                    cur.execute(qry)
                    con.commit()

def drug_reaction_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='reactions':
            for j in range(0,len(root[x])):
                seq=root[x][j][0].text
                left_drug_id=root[x][j][1][0].text
                left_drug_element=root[x][j][1][1].text
                right_drug_id=root[x][j][2][0].text
                right_drug_element=root[x][j][2][1].text
                qry = "set nocount off set ansi_warnings off insert into  drug_reactions select '"+primary_id+"','"+str(j+1)+"','"+seq+"','"+left_drug_id+"','"+left_drug_element+"','"+right_drug_id+"','"+right_drug_element+"' where not exists(select drug_id from drug_reactions where drug_id='"+primary_id+"' and drugr_id='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()
                inx=0
                while root[x][j][inx].tag!='enzymes':
                    inx=inx+1;
                for i in range(0,len(root[x][j][inx])):
                    drugbank_id=root[x][j][inx][i][0].text
                    enzyme_reaction=root[x][j][inx][i][1].text
                    uniprot_id=root[x][j][inx][i][2].text
                    qry = "set nocount off set ansi_warnings off insert into  drug_reactions_enzymes select '"+str(j+1)+"','"+str(i+1)+"','"+primary_id+"','"+drugbank_id+"','"+enzyme_reaction+"','"+uniprot_id+"' where not exists(select drug_id from drug_reactions_enzymes where drug_id='"+primary_id+"' and counter='"+str(i+1)+"' and drugr_id='"+str(j+1)+"')"
                    cur.execute(qry)
                    con.commit()
                
def drug_snp_effects_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='snp-effects':
            for j in range(0,len(root[x])):
                p_name=root[x][j][0].text
                g_symbol=root[x][j][1].text
                uniprot_id=root[x][j][2].text
                rs_id=root[x][j][3].text
                allele=root[x][j][4].text
                defining_chance=root[x][j][5].text
                description=root[x][j][6].text
                pubmed_id=root[x][j][7].text
                qry = "set nocount off set ansi_warnings off insert into  drug_snp_effects select '"+primary_id+"','"+str(j+1)+"','"+p_name+"','"+g_symbol+"','"+uniprot_id+"','"+rs_id+"','"+allele+"','"+defining_chance+"','"+description+"','"+pubmed_id+"' where not exists(select drug_id from drug_snp_effects where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()
                
def drug_snp_adverse_reaction_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='snp-adverse-drug-reactions':
            for j in range(0,len(root[x])):
                p_name=root[x][j][0].text
                g_symbol=root[x][j][1].text
                uniprot_id=root[x][j][2].text
                rs_id=root[x][j][3].text
                allele=root[x][j][4].text
                adverse_reaction=root[x][j][5].text
                description=root[x][j][6].text
                pubmed_id=root[x][j][7].text
                qry = "set nocount off set ansi_warnings off insert into  drug_snp_adverse_reaction select '"+primary_id+"','"+str(j+1)+"','"+p_name+"','"+g_symbol+"','"+uniprot_id+"','"+rs_id+"','"+allele+"','"+adverse_reaction+"','"+description+"','"+pubmed_id+"' where not exists(select drug_id from drug_snp_adverse_reaction where drug_id='"+primary_id+"' and counter='"+str(j+1)+"')"
                cur.execute(qry)
                con.commit()

def drug_targets_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                position=-1
                if 'position' in (root[x][j].attrib):
                    position=root[x][j].attrib['position']
                inx=0
                while root[x][j][inx].tag!='id':
                    inx=inx+1
                target_id=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='name':
                    inx=inx+1
                target_name=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='organism':
                    inx=inx+1
                organism=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='known-action':
                    inx=inx+1
                known_action=root[x][j][inx].text
                qry = "set nocount off set ansi_warnings off insert into  drug_targets select '"+primary_id+"','"+str(position)+"','"+target_id+"','"+target_name+"','"+organism+"','"+known_action+"' where not exists(select drug_id from drug_targets where drug_id='"+primary_id+"' and target_id='"+target_id+"')"
                if target_id not in ls:
                    ls.append(target_id)
                    cur.execute(qry)
                    con.commit()

def drug_targets_actions_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                position=-1
                m=0
                while root[x][j][m].tag!='actions':
                    m=m+1
                target_id=root[x][j][0].text
                if target_id not in ls:
                    ls.append(target_id)
                    for i in range(0,len(root[x][j][m])):
                        target_action=root[x][j][m][i].text
                        qry = "set nocount off set ansi_warnings off insert into  drug_target_actions select '"+primary_id+"','"+target_id+"','"+str(i+1)+"','"+target_action+"' where not exists(select drug_id from drug_target_actions where drug_id='"+primary_id+"' and counter='"+str(i+1)+"' and target_id='"+target_id+"')"
                        cur.execute(qry)
                        con.commit()

def drug_target_reference_article_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='articles':
                                for r in range(0,len(root[x][j][m][i])):
                                    pub_id=root[x][j][m][i][r][0].text
                                    cite=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_target_articles select '"+primary_id+"','"+target_id+"','"+pub_id+"','"+cite+"' where not exists(select drug_id from drug_target_articles where drug_id='"+primary_id+"' and pubmed_id='"+pub_id+"' and target_id='"+target_id+"')"
                                    cur.execute(qry)
                                    con.commit()
                

def drug_target_reference_text_book_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='textbooks':
                                for r in range(0,len(root[x][j][m][i])):
                                    isbn=root[x][j][m][i][r][0].text
                                    cite=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_target_books select '"+primary_id+"','"+str(r+1)+"','"+target_id+"','"+isbn+"','"+cite+"' where not exists(select drug_id from drug_target_books where drug_id='"+primary_id+"' and isbn='"+isbn+"' and counter='"+str(r+1)+"' and target_id='"+target_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_target_reference_text_link_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='links':
                                for r in range(0,len(root[x][j][m][i])):
                                    title=root[x][j][m][i][r][0].text
                                    url=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_target_links select '"+primary_id+"','"+target_id+"','"+title+"','"+url+"' where not exists(select drug_id from drug_target_links where drug_id='"+primary_id+"' and title='"+title+"' and url='"+url+"' and target_id='"+target_id+"')"
                                    cur.execute(qry)
                                    con.commit()


def drug_targets_polypeptide_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if (root[x][j][m].tag=='polypeptide'):
                        poly_id='no id';
                        if 'id' in (root[x][j][m].attrib):
                            poly_id=root[x][j][m].attrib['id']
                        src='no source';
                        if 'source' in (root[x][j][m].attrib):
                            src=root[x][j][m].attrib['source']
                        inx=0
                        while root[x][j][m][inx].tag!='name':
                            inx=inx+1
                        poly_name=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='general-function':
                            inx=inx+1
                        general_function=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='specific-function':
                            inx=inx+1
                        specific_function=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='gene-name':
                            inx=inx+1
                        gene_name=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='locus':
                            inx=inx+1
                        locus=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='cellular-location':
                            inx=inx+1
                        cellular_location=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='theoretical-pi':
                            inx=inx+1
                        pi=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='molecular-weight':
                            inx=inx+1
                        molecular_weight=root[x][j][m][inx].text
                        if molecular_weight=="null":
                            molecular_weight="0"
                        inx=0
                        while root[x][j][m][inx].tag!='chromosome-location':
                            inx=inx+1
                        location=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='organism':
                            inx=inx+1
                        organism=root[x][j][m][inx].text
                        ncbi_t_id='no id'
                        if 'ncbi-taxonomy-id' in (root[x][j][m][inx].attrib):
                            ncbi_t_id=root[x][j][m][inx].attrib['ncbi-taxonomy-id']
                        qry = "set nocount off set ansi_warnings off insert into  drug_target_polypeptide select '"+primary_id+"','"+target_id+"','"+poly_id+"','"+src+"','"+poly_name+"','"+general_function+"','"+specific_function+"','"+gene_name+"','"+locus+"','"+cellular_location+"','"+pi+"','"+molecular_weight+"','"+location+"','"+ncbi_t_id+"','"+organism+"' where not exists(select drug_id from drug_target_polypeptide where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and target_id='"+target_id+"')"
                        cur.execute(qry)
                        con.commit()
                        inx=0
                        while root[x][j][m][inx].tag!='transmembrane-regions':
                            inx=inx+1
                        s=root[x][j][m][inx].text
                        s=s.strip()
                        s.replace('\t','')
                        ls=s.split('\n')
                        for d in range(0,len(ls)):
                            qry = "set nocount off set ansi_warnings off insert into  drug_target_polypeptide_transmembrance select '"+primary_id+"','"+target_id+"','"+poly_id+"','"+ls[d]+"' where not exists(select drug_id from drug_target_polypeptide_transmembrance where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and target_id='"+target_id+"')"
                            cur.execute(qry)
                            con.commit()
                        inx=0
                        while root[x][j][m][inx].tag!='signal-regions':
                            inx=inx+1
                        s=root[x][j][m][inx].text
                        s=s.strip()
                        s.replace('\t','')
                        ls=s.split('\n')
                        for d in range(0,len(ls)):
                            qry = "set nocount off set ansi_warnings off insert into  drug_target_polypeptide_signal select '"+primary_id+"','"+target_id+"','"+poly_id+"','"+ls[d]+"' where not exists(select drug_id from drug_target_polypeptide_signal where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and regions='"+ls[d]+"' and target_id='"+target_id+"')"
                            cur.execute(qry)
                            con.commit()
                    

def drug_target_poly_synonyms_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='synonyms':
                                for r in range(0,len(root[x][j][m][i])):
                                    lan=''
                                    if 'language' in (root[x][j][m][i][r].attrib):
                                        lan=root[x][j][m][i][r].attrib['language']
                                    coder=''
                                    if 'coder' in (root[x][j][m][i][r].attrib):
                                        coder=root[x][j][m][i][r].attrib['language']
                                    synonym=root[x][j][m][i][r].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_target_poly_synonyms select '"+primary_id+"','"+target_id+"','"+str(r+1)+"','"+poly_id+"','"+lan+"','"+coder+"','"+synonym+"' where not exists(select drug_id from drug_target_poly_synonyms where drug_id='"+primary_id+"' and counter='"+str(r+1)+"' and polypeptide_id='"+poly_id+"' and target_id='"+target_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_target_poly_ex_iden_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='external-identifiers':
                                for r in range(0,len(root[x][j][m][i])):
                                    rsc=root[x][j][m][i][r][0].text
                                    identifier=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_target_poly_ex_iden select '"+primary_id+"','"+target_id+"','"+poly_id+"','"+str(r+1)+"','"+rsc+"','"+identifier+"' where not exists(select drug_id from drug_target_poly_ex_iden where drug_id='"+primary_id+"' and counter='"+str(r+1)+"' and polypeptide_id='"+poly_id+"' and target_id='"+target_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_target_poly_aminoacid_seq_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='amino-acid-sequence':
                                seq=root[x][j][m][i].text
                                frm=''
                                if 'format' in (root[x][j][m][i].attrib):
                                    frm=root[x][j][m][i].attrib['format']
                                qry = "set nocount off set ansi_warnings off insert into  drug_target_poly_aminoacid_seq select '"+primary_id+"','"+target_id+"','"+poly_id+"','"+frm+"','"+seq+"' where not exists(select drug_id from drug_target_poly_aminoacid_seq where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and target_id='"+target_id+"')"
                                cur.execute(qry)
                                con.commit()

def drug_target_poly_gene_seq_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='gene-sequence':
                                seq=root[x][j][m][i].text
                                frm=''
                                if 'format' in (root[x][j][m][i].attrib):
                                    frm=root[x][j][m][i].attrib['format']
                                qry = "set nocount off set ansi_warnings off insert into  drug_target_poly_gene_seq select '"+primary_id+"','"+target_id+"','"+poly_id+"','"+frm+"','"+seq+"' where not exists(select drug_id from drug_target_poly_gene_seq where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and target_id='"+target_id+"')"
                                cur.execute(qry)
                                con.commit()

def drug_target_poly_pfams_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='pfams':
                                for r in range(0,len(root[x][j][m][i])):
                                    pfam_identifier=root[x][j][m][i][r][0].text
                                    pfam_name=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_target_poly_pfams select '"+primary_id+"','"+target_id+"','"+poly_id+"','"+pfam_name+"','"+pfam_identifier+"' where not exists(select drug_id from drug_target_poly_pfams where drug_id='"+primary_id+"' and identifier='"+pfam_identifier+"' and polypeptide_id='"+poly_id+"' and target_id='"+target_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_target_poly_go_classifier_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='targets':
            for j in range(0,len(root[x])):
                target_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='go-classifiers':
                                for r in range(0,len(root[x][j][m][i])):
                                    category=root[x][j][m][i][r][0].text
                                    description=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_target_poly_go_classfier select '"+primary_id+"','"+target_id+"','"+poly_id+"','"+category+"','"+description+"' where not exists(select drug_id from drug_target_poly_go_classfier where drug_id='"+primary_id+"' and category='"+category+"' and classifier_description='"+description+"' and polypeptide_id='"+poly_id+"' and target_id='"+target_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_enzymes_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                position=-1
                if 'position' in (root[x][j].attrib):
                    position=root[x][j].attrib['position']
                inx=0
                while root[x][j][inx].tag!='id':
                    inx=inx+1
                enzyme_id=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='name':
                    inx=inx+1
                enzyme_name=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='organism':
                    inx=inx+1
                organism=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='known-action':
                    inx=inx+1
                known_action=root[x][j][inx].text
                while root[x][j][inx].tag!='inhibition-strength':
                    inx=inx+1
                inhibition=root[x][j][inx].text
                while root[x][j][inx].tag!='induction-strength':
                    inx=inx+1
                induction=root[x][j][inx].text
                qry = "set nocount off set ansi_warnings off insert into  drug_enzymes select '"+primary_id+"','"+str(position)+"','"+enzyme_id+"','"+enzyme_name+"','"+organism+"','"+known_action+"','"+inhibition+"','"+induction+"' where not exists(select drug_id from drug_enzymes where drug_id='"+primary_id+"' and enzyme_id='"+enzyme_id+"')"
                if enzyme_id not in ls:
                    ls.append(enzyme_id)
                    cur.execute(qry)
                    con.commit()

def drug_enzymes_actions_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                position=-1
                m=0
                while root[x][j][m].tag!='actions':
                    m=m+1
                enzyme_id=root[x][j][0].text
                if enzyme_id not in ls:
                    ls.append(enzyme_id)
                    for i in range(0,len(root[x][j][m])):
                        enzyme_action=root[x][j][m][i].text
                        qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_actions select '"+primary_id+"','"+enzyme_id+"','"+str(i+1)+"','"+enzyme_action+"' where not exists(select drug_id from drug_enzyme_actions where drug_id='"+primary_id+"' and counter='"+str(i+1)+"' and enzyme_id='"+enzyme_id+"')"
                        cur.execute(qry)
                        con.commit()

def drug_enzyme_reference_article_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='articles':
                                for r in range(0,len(root[x][j][m][i])):
                                    pub_id=root[x][j][m][i][r][0].text
                                    cite=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_articles select '"+primary_id+"','"+enzyme_id+"','"+pub_id+"','"+cite+"' where not exists(select drug_id from drug_enzyme_articles where drug_id='"+primary_id+"' and pubmed_id='"+pub_id+"' and enzyme_id='"+enzyme_id+"')"
                                    cur.execute(qry)
                                    con.commit()
                

def drug_enzyme_reference_text_book_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='textbooks':
                                for r in range(0,len(root[x][j][m][i])):
                                    isbn=root[x][j][m][i][r][0].text
                                    cite=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_books select '"+primary_id+"','"+str(r+1)+"','"+enzyme_id+"','"+isbn+"','"+cite+"' where not exists(select drug_id from drug_enzyme_books where drug_id='"+primary_id+"' and isbn='"+isbn+"' and counter='"+str(r+1)+"' and enzyme_id='"+enzyme_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_enzyme_reference_text_link_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='links':
                                for r in range(0,len(root[x][j][m][i])):
                                    title=root[x][j][m][i][r][0].text
                                    url=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_links select '"+primary_id+"','"+enzyme_id+"','"+title+"','"+url+"' where not exists(select drug_id from drug_enzyme_links where drug_id='"+primary_id+"' and title='"+title+"' and url='"+url+"' and enzyme_id='"+enzyme_id+"')"
                                    cur.execute(qry)
                                    con.commit()


def drug_enzymes_polypeptide_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if (root[x][j][m].tag=='polypeptide'):
                        poly_id='no id';
                        if 'id' in (root[x][j][m].attrib):
                            poly_id=root[x][j][m].attrib['id']
                        src='no source';
                        if 'source' in (root[x][j][m].attrib):
                            src=root[x][j][m].attrib['source']
                        inx=0
                        while root[x][j][m][inx].tag!='name':
                            inx=inx+1
                        poly_name=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='general-function':
                            inx=inx+1
                        general_function=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='specific-function':
                            inx=inx+1
                        specific_function=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='gene-name':
                            inx=inx+1
                        gene_name=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='locus':
                            inx=inx+1
                        locus=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='cellular-location':
                            inx=inx+1
                        cellular_location=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='theoretical-pi':
                            inx=inx+1
                        pi=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='molecular-weight':
                            inx=inx+1
                        molecular_weight=root[x][j][m][inx].text
                        if molecular_weight=="null":
                            molecular_weight="0"
                        inx=0
                        while root[x][j][m][inx].tag!='chromosome-location':
                            inx=inx+1
                        location=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='organism':
                            inx=inx+1
                        organism=root[x][j][m][inx].text
                        ncbi_t_id='no id'
                        if 'ncbi-taxonomy-id' in (root[x][j][m][inx].attrib):
                            ncbi_t_id=root[x][j][m][inx].attrib['ncbi-taxonomy-id']
                        qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_polypeptide select '"+primary_id+"','"+enzyme_id+"','"+poly_id+"','"+src+"','"+poly_name+"','"+general_function+"','"+specific_function+"','"+gene_name+"','"+locus+"','"+cellular_location+"','"+pi+"','"+molecular_weight+"','"+location+"','"+ncbi_t_id+"','"+organism+"' where not exists(select drug_id from drug_enzyme_polypeptide where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and enzyme_id='"+enzyme_id+"')"
                        cur.execute(qry)
                        con.commit()
                        inx=0
                        while root[x][j][m][inx].tag!='transmembrane-regions':
                            inx=inx+1
                        s=root[x][j][m][inx].text
                        s=s.strip()
                        s.replace('\t','')
                        ls=s.split('\n')
                        for d in range(0,len(ls)):
                            qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_polypeptide_transmembrance select '"+primary_id+"','"+enzyme_id+"','"+poly_id+"','"+ls[d]+"' where not exists(select drug_id from drug_enzyme_polypeptide_transmembrance where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and enzyme_id='"+enzyme_id+"')"
                            cur.execute(qry)
                            con.commit()
                        inx=0
                        while root[x][j][m][inx].tag!='signal-regions':
                            inx=inx+1
                        s=root[x][j][m][inx].text
                        s=s.strip()
                        s.replace('\t','')
                        ls=s.split('\n')
                        for d in range(0,len(ls)):
                            qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_polypeptide_signal select '"+primary_id+"','"+enzyme_id+"','"+poly_id+"','"+ls[d]+"' where not exists(select drug_id from drug_enzyme_polypeptide_signal where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and regions='"+ls[d]+"' and enzyme_id='"+enzyme_id+"')"
                            cur.execute(qry)
                            con.commit()
                    

def drug_enzyme_poly_synonyms_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='synonyms':
                                for r in range(0,len(root[x][j][m][i])):
                                    lan=''
                                    if 'language' in (root[x][j][m][i][r].attrib):
                                        lan=root[x][j][m][i][r].attrib['language']
                                    coder=''
                                    if 'coder' in (root[x][j][m][i][r].attrib):
                                        coder=root[x][j][m][i][r].attrib['language']
                                    synonym=root[x][j][m][i][r].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_poly_synonyms select '"+primary_id+"','"+enzyme_id+"','"+str(r+1)+"','"+poly_id+"','"+lan+"','"+coder+"','"+synonym+"' where not exists(select drug_id from drug_enzyme_poly_synonyms where drug_id='"+primary_id+"' and counter='"+str(r+1)+"' and polypeptide_id='"+poly_id+"' and enzyme_id='"+enzyme_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_enzyme_poly_ex_iden_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='external-identifiers':
                                for r in range(0,len(root[x][j][m][i])):
                                    rsc=root[x][j][m][i][r][0].text
                                    identifier=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_poly_ex_iden select '"+primary_id+"','"+enzyme_id+"','"+poly_id+"','"+str(r+1)+"','"+rsc+"','"+identifier+"' where not exists(select drug_id from drug_enzyme_poly_ex_iden where drug_id='"+primary_id+"' and counter='"+str(r+1)+"' and polypeptide_id='"+poly_id+"' and enzyme_id='"+enzyme_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_enzyme_poly_aminoacid_seq_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='amino-acid-sequence':
                                seq=root[x][j][m][i].text
                                frm=''
                                if 'format' in (root[x][j][m][i].attrib):
                                    frm=root[x][j][m][i].attrib['format']
                                qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_poly_aminoacid_seq select '"+primary_id+"','"+enzyme_id+"','"+poly_id+"','"+frm+"','"+seq+"' where not exists(select drug_id from drug_enzyme_poly_aminoacid_seq where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and enzyme_id='"+enzyme_id+"')"
                                cur.execute(qry)
                                con.commit()

def drug_enzyme_poly_gene_seq_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='gene-sequence':
                                seq=root[x][j][m][i].text
                                frm=''
                                if 'format' in (root[x][j][m][i].attrib):
                                    frm=root[x][j][m][i].attrib['format']
                                qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_poly_gene_seq select '"+primary_id+"','"+enzyme_id+"','"+poly_id+"','"+frm+"','"+seq+"' where not exists(select drug_id from drug_enzyme_poly_gene_seq where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and enzyme_id='"+enzyme_id+"')"
                                cur.execute(qry)
                                con.commit()

def drug_enzyme_poly_pfams_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='pfams':
                                for r in range(0,len(root[x][j][m][i])):
                                    pfam_identifier=root[x][j][m][i][r][0].text
                                    pfam_name=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_poly_pfams select '"+primary_id+"','"+enzyme_id+"','"+poly_id+"','"+pfam_name+"','"+pfam_identifier+"' where not exists(select drug_id from drug_enzyme_poly_pfams where drug_id='"+primary_id+"' and identifier='"+pfam_identifier+"' and polypeptide_id='"+poly_id+"' and enzyme_id='"+enzyme_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_enzyme_poly_go_classifier_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='enzymes':
            for j in range(0,len(root[x])):
                enzyme_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='go-classifiers':
                                for r in range(0,len(root[x][j][m][i])):
                                    category=root[x][j][m][i][r][0].text
                                    description=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_enzyme_poly_go_classfier select '"+primary_id+"','"+enzyme_id+"','"+poly_id+"','"+category+"','"+description+"' where not exists(select drug_id from drug_enzyme_poly_go_classfier where drug_id='"+primary_id+"' and category='"+category+"' and classifier_description='"+description+"' and polypeptide_id='"+poly_id+"' and enzyme_id='"+enzyme_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_carriers_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                position=-1
                if 'position' in (root[x][j].attrib):
                    position=root[x][j].attrib['position']
                inx=0
                while root[x][j][inx].tag!='id':
                    inx=inx+1
                carrier_id=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='name':
                    inx=inx+1
                carrier_name=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='organism':
                    inx=inx+1
                organism=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='known-action':
                    inx=inx+1
                known_action=root[x][j][inx].text
                qry = "set nocount off set ansi_warnings off insert into  drug_carriers select '"+primary_id+"','"+str(position)+"','"+carrier_id+"','"+carrier_name+"','"+organism+"','"+known_action+"' where not exists(select drug_id from drug_carriers where drug_id='"+primary_id+"' and carrier_id='"+carrier_id+"')"
                if carrier_id not in ls:
                    ls.append(carrier_id)
                    cur.execute(qry)
                    con.commit()

def drug_carriers_actions_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                position=-1
                m=0
                while root[x][j][m].tag!='actions':
                    m=m+1
                carrier_id=root[x][j][0].text
                if carrier_id not in ls:
                    ls.append(carrier_id)
                    for i in range(0,len(root[x][j][m])):
                        carrier_action=root[x][j][m][i].text
                        qry = "set nocount off set ansi_warnings off insert into  drug_carrier_actions select '"+primary_id+"','"+carrier_id+"','"+str(i+1)+"','"+carrier_action+"' where not exists(select drug_id from drug_carrier_actions where drug_id='"+primary_id+"' and counter='"+str(i+1)+"' and carrier_id='"+carrier_id+"')"
                        cur.execute(qry)
                        con.commit()

def drug_carrier_reference_article_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='articles':
                                for r in range(0,len(root[x][j][m][i])):
                                    pub_id=root[x][j][m][i][r][0].text
                                    cite=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_carrier_articles select '"+primary_id+"','"+carrier_id+"','"+pub_id+"','"+cite+"' where not exists(select drug_id from drug_carrier_articles where drug_id='"+primary_id+"' and pubmed_id='"+pub_id+"' and carrier_id='"+carrier_id+"')"
                                    cur.execute(qry)
                                    con.commit()
                

def drug_carrier_reference_text_book_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='textbooks':
                                for r in range(0,len(root[x][j][m][i])):
                                    isbn=root[x][j][m][i][r][0].text
                                    cite=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_carrier_books select '"+primary_id+"','"+str(r+1)+"','"+carrier_id+"','"+isbn+"','"+cite+"' where not exists(select drug_id from drug_carrier_books where drug_id='"+primary_id+"' and isbn='"+isbn+"' and counter='"+str(r+1)+"' and carrier_id='"+carrier_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_carrier_reference_text_link_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='links':
                                for r in range(0,len(root[x][j][m][i])):
                                    title=root[x][j][m][i][r][0].text
                                    url=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_carrier_links select '"+primary_id+"','"+carrier_id+"','"+title+"','"+url+"' where not exists(select drug_id from drug_carrier_links where drug_id='"+primary_id+"' and title='"+title+"' and url='"+url+"' and carrier_id='"+carrier_id+"')"
                                    cur.execute(qry)
                                    con.commit()


def drug_carriers_polypeptide_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if (root[x][j][m].tag=='polypeptide'):
                        poly_id='no id';
                        if 'id' in (root[x][j][m].attrib):
                            poly_id=root[x][j][m].attrib['id']
                        src='no source';
                        if 'source' in (root[x][j][m].attrib):
                            src=root[x][j][m].attrib['source']
                        inx=0
                        while root[x][j][m][inx].tag!='name':
                            inx=inx+1
                        poly_name=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='general-function':
                            inx=inx+1
                        general_function=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='specific-function':
                            inx=inx+1
                        specific_function=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='gene-name':
                            inx=inx+1
                        gene_name=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='locus':
                            inx=inx+1
                        locus=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='cellular-location':
                            inx=inx+1
                        cellular_location=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='theoretical-pi':
                            inx=inx+1
                        pi=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='molecular-weight':
                            inx=inx+1
                        molecular_weight=root[x][j][m][inx].text
                        if molecular_weight=="null":
                            molecular_weight="0"
                        inx=0
                        while root[x][j][m][inx].tag!='chromosome-location':
                            inx=inx+1
                        location=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='organism':
                            inx=inx+1
                        organism=root[x][j][m][inx].text
                        ncbi_t_id='no id'
                        if 'ncbi-taxonomy-id' in (root[x][j][m][inx].attrib):
                            ncbi_t_id=root[x][j][m][inx].attrib['ncbi-taxonomy-id']
                        qry = "set nocount off set ansi_warnings off insert into  drug_carrier_polypeptide select '"+primary_id+"','"+carrier_id+"','"+poly_id+"','"+src+"','"+poly_name+"','"+general_function+"','"+specific_function+"','"+gene_name+"','"+locus+"','"+cellular_location+"','"+pi+"','"+molecular_weight+"','"+location+"','"+ncbi_t_id+"','"+organism+"' where not exists(select drug_id from drug_carrier_polypeptide where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and carrier_id='"+carrier_id+"')"
                        cur.execute(qry)
                        con.commit()
                        inx=0
                        while root[x][j][m][inx].tag!='transmembrane-regions':
                            inx=inx+1
                        s=root[x][j][m][inx].text
                        s=s.strip()
                        s.replace('\t','')
                        ls=s.split('\n')
                        for d in range(0,len(ls)):
                            qry = "set nocount off set ansi_warnings off insert into  drug_carrier_polypeptide_transmembrance select '"+primary_id+"','"+carrier_id+"','"+poly_id+"','"+ls[d]+"' where not exists(select drug_id from drug_carrier_polypeptide_transmembrance where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and carrier_id='"+carrier_id+"')"
                            cur.execute(qry)
                            con.commit()
                        inx=0
                        while root[x][j][m][inx].tag!='signal-regions':
                            inx=inx+1
                        s=root[x][j][m][inx].text
                        s=s.strip()
                        s.replace('\t','')
                        ls=s.split('\n')
                        for d in range(0,len(ls)):
                            qry = "set nocount off set ansi_warnings off insert into  drug_carrier_polypeptide_signal select '"+primary_id+"','"+carrier_id+"','"+poly_id+"','"+ls[d]+"' where not exists(select drug_id from drug_carrier_polypeptide_signal where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and regions='"+ls[d]+"' and carrier_id='"+carrier_id+"')"
                            cur.execute(qry)
                            con.commit()
                    

def drug_carrier_poly_synonyms_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='synonyms':
                                for r in range(0,len(root[x][j][m][i])):
                                    lan=''
                                    if 'language' in (root[x][j][m][i][r].attrib):
                                        lan=root[x][j][m][i][r].attrib['language']
                                    coder=''
                                    if 'coder' in (root[x][j][m][i][r].attrib):
                                        coder=root[x][j][m][i][r].attrib['language']
                                    synonym=root[x][j][m][i][r].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_carrier_poly_synonyms select '"+primary_id+"','"+carrier_id+"','"+str(r+1)+"','"+poly_id+"','"+lan+"','"+coder+"','"+synonym+"' where not exists(select drug_id from drug_carrier_poly_synonyms where drug_id='"+primary_id+"' and counter='"+str(r+1)+"' and polypeptide_id='"+poly_id+"' and carrier_id='"+carrier_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_carrier_poly_ex_iden_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='external-identifiers':
                                for r in range(0,len(root[x][j][m][i])):
                                    rsc=root[x][j][m][i][r][0].text
                                    identifier=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_carrier_poly_ex_iden select '"+primary_id+"','"+carrier_id+"','"+poly_id+"','"+str(r+1)+"','"+rsc+"','"+identifier+"' where not exists(select drug_id from drug_carrier_poly_ex_iden where drug_id='"+primary_id+"' and counter='"+str(r+1)+"' and polypeptide_id='"+poly_id+"' and carrier_id='"+carrier_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_carrier_poly_aminoacid_seq_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='amino-acid-sequence':
                                seq=root[x][j][m][i].text
                                frm=''
                                if 'format' in (root[x][j][m][i].attrib):
                                    frm=root[x][j][m][i].attrib['format']
                                qry = "set nocount off set ansi_warnings off insert into  drug_carrier_poly_aminoacid_seq select '"+primary_id+"','"+carrier_id+"','"+poly_id+"','"+frm+"','"+seq+"' where not exists(select drug_id from drug_carrier_poly_aminoacid_seq where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and carrier_id='"+carrier_id+"')"
                                cur.execute(qry)
                                con.commit()

def drug_carrier_poly_gene_seq_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='gene-sequence':
                                seq=root[x][j][m][i].text
                                frm=''
                                if 'format' in (root[x][j][m][i].attrib):
                                    frm=root[x][j][m][i].attrib['format']
                                qry = "set nocount off set ansi_warnings off insert into  drug_carrier_poly_gene_seq select '"+primary_id+"','"+carrier_id+"','"+poly_id+"','"+frm+"','"+seq+"' where not exists(select drug_id from drug_carrier_poly_gene_seq where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and carrier_id='"+carrier_id+"')"
                                cur.execute(qry)
                                con.commit()

def drug_carrier_poly_pfams_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='pfams':
                                for r in range(0,len(root[x][j][m][i])):
                                    pfam_identifier=root[x][j][m][i][r][0].text
                                    pfam_name=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_carrier_poly_pfams select '"+primary_id+"','"+carrier_id+"','"+poly_id+"','"+pfam_name+"','"+pfam_identifier+"' where not exists(select drug_id from drug_carrier_poly_pfams where drug_id='"+primary_id+"' and identifier='"+pfam_identifier+"' and polypeptide_id='"+poly_id+"' and carrier_id='"+carrier_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_carrier_poly_go_classifier_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='carriers':
            for j in range(0,len(root[x])):
                carrier_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='go-classifiers':
                                for r in range(0,len(root[x][j][m][i])):
                                    category=root[x][j][m][i][r][0].text
                                    description=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_carrier_poly_go_classfier select '"+primary_id+"','"+carrier_id+"','"+poly_id+"','"+category+"','"+description+"' where not exists(select drug_id from drug_carrier_poly_go_classfier where drug_id='"+primary_id+"' and category='"+category+"' and classifier_description='"+description+"' and polypeptide_id='"+poly_id+"' and carrier_id='"+carrier_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_transporters_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                position=-1
                if 'position' in (root[x][j].attrib):
                    position=root[x][j].attrib['position']
                inx=0
                while root[x][j][inx].tag!='id':
                    inx=inx+1
                transporter_id=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='name':
                    inx=inx+1
                transporter_name=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='organism':
                    inx=inx+1
                organism=root[x][j][inx].text
                inx=0
                while root[x][j][inx].tag!='known-action':
                    inx=inx+1
                known_action=root[x][j][inx].text
                qry = "set nocount off set ansi_warnings off insert into  drug_transporters select '"+primary_id+"','"+str(position)+"','"+transporter_id+"','"+transporter_name+"','"+organism+"','"+known_action+"' where not exists(select drug_id from drug_transporters where drug_id='"+primary_id+"' and transporter_id='"+transporter_id+"')"
                if transporter_id not in ls:
                    ls.append(transporter_id)
                    cur.execute(qry)
                    con.commit()

def drug_transporters_actions_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                position=-1
                m=0
                while root[x][j][m].tag!='actions':
                    m=m+1
                transporter_id=root[x][j][0].text
                if transporter_id not in ls:
                    ls.append(transporter_id)
                    for i in range(0,len(root[x][j][m])):
                        transporter_action=root[x][j][m][i].text
                        qry = "set nocount off set ansi_warnings off insert into  drug_transporter_actions select '"+primary_id+"','"+transporter_id+"','"+str(i+1)+"','"+transporter_action+"' where not exists(select drug_id from drug_transporter_actions where drug_id='"+primary_id+"' and counter='"+str(i+1)+"' and transporter_id='"+transporter_id+"')"
                        cur.execute(qry)
                        con.commit()

def drug_transporter_reference_article_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='articles':
                                for r in range(0,len(root[x][j][m][i])):
                                    pub_id=root[x][j][m][i][r][0].text
                                    cite=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_transporter_articles select '"+primary_id+"','"+transporter_id+"','"+pub_id+"','"+cite+"' where not exists(select drug_id from drug_transporter_articles where drug_id='"+primary_id+"' and pubmed_id='"+pub_id+"' and transporter_id='"+transporter_id+"')"
                                    cur.execute(qry)
                                    con.commit()
                

def drug_transporter_reference_text_book_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='textbooks':
                                for r in range(0,len(root[x][j][m][i])):
                                    isbn=root[x][j][m][i][r][0].text
                                    cite=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_transporter_books select '"+primary_id+"','"+str(r+1)+"','"+transporter_id+"','"+isbn+"','"+cite+"' where not exists(select drug_id from drug_transporter_books where drug_id='"+primary_id+"' and isbn='"+isbn+"' and counter='"+str(r+1)+"' and transporter_id='"+transporter_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_transporter_reference_text_link_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='references':
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='links':
                                for r in range(0,len(root[x][j][m][i])):
                                    title=root[x][j][m][i][r][0].text
                                    url=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_transporter_links select '"+primary_id+"','"+transporter_id+"','"+title+"','"+url+"' where not exists(select drug_id from drug_transporter_links where drug_id='"+primary_id+"' and title='"+title+"' and url='"+url+"' and transporter_id='"+transporter_id+"')"
                                    cur.execute(qry)
                                    con.commit()


def drug_transporters_polypeptide_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    ls=[]
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if (root[x][j][m].tag=='polypeptide'):
                        poly_id='no id';
                        if 'id' in (root[x][j][m].attrib):
                            poly_id=root[x][j][m].attrib['id']
                        src='no source';
                        if 'source' in (root[x][j][m].attrib):
                            src=root[x][j][m].attrib['source']
                        inx=0
                        while root[x][j][m][inx].tag!='name':
                            inx=inx+1
                        poly_name=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='general-function':
                            inx=inx+1
                        general_function=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='specific-function':
                            inx=inx+1
                        specific_function=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='gene-name':
                            inx=inx+1
                        gene_name=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='locus':
                            inx=inx+1
                        locus=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='cellular-location':
                            inx=inx+1
                        cellular_location=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='theoretical-pi':
                            inx=inx+1
                        pi=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='molecular-weight':
                            inx=inx+1
                        molecular_weight=root[x][j][m][inx].text
                        if molecular_weight=="null":
                            molecular_weight="0"
                        inx=0
                        while root[x][j][m][inx].tag!='chromosome-location':
                            inx=inx+1
                        location=root[x][j][m][inx].text
                        inx=0
                        while root[x][j][m][inx].tag!='organism':
                            inx=inx+1
                        organism=root[x][j][m][inx].text
                        ncbi_t_id='no id'
                        if 'ncbi-taxonomy-id' in (root[x][j][m][inx].attrib):
                            ncbi_t_id=root[x][j][m][inx].attrib['ncbi-taxonomy-id']
                        qry = "set nocount off set ansi_warnings off insert into  drug_transporter_polypeptide select '"+primary_id+"','"+transporter_id+"','"+poly_id+"','"+src+"','"+poly_name+"','"+general_function+"','"+specific_function+"','"+gene_name+"','"+locus+"','"+cellular_location+"','"+pi+"','"+molecular_weight+"','"+location+"','"+ncbi_t_id+"','"+organism+"' where not exists(select drug_id from drug_transporter_polypeptide where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and transporter_id='"+transporter_id+"')"
                        cur.execute(qry)
                        con.commit()
                        inx=0
                        while root[x][j][m][inx].tag!='transmembrane-regions':
                            inx=inx+1
                        s=root[x][j][m][inx].text
                        s=s.strip()
                        s.replace('\t','')
                        ls=s.split('\n')
                        for d in range(0,len(ls)):
                            qry = "set nocount off set ansi_warnings off insert into  drug_transporter_polypeptide_transmembrance select '"+primary_id+"','"+transporter_id+"','"+poly_id+"','"+ls[d]+"' where not exists(select drug_id from drug_transporter_polypeptide_transmembrance where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and transporter_id='"+transporter_id+"')"
                            cur.execute(qry)
                            con.commit()
                        inx=0
                        while root[x][j][m][inx].tag!='signal-regions':
                            inx=inx+1
                        s=root[x][j][m][inx].text
                        s=s.strip()
                        s.replace('\t','')
                        ls=s.split('\n')
                        for d in range(0,len(ls)):
                            qry = "set nocount off set ansi_warnings off insert into  drug_transporter_polypeptide_signal select '"+primary_id+"','"+transporter_id+"','"+poly_id+"','"+ls[d]+"' where not exists(select drug_id from drug_transporter_polypeptide_signal where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and regions='"+ls[d]+"' and transporter_id='"+transporter_id+"')"
                            cur.execute(qry)
                            con.commit()
                    

def drug_transporter_poly_synonyms_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='synonyms':
                                for r in range(0,len(root[x][j][m][i])):
                                    lan=''
                                    if 'language' in (root[x][j][m][i][r].attrib):
                                        lan=root[x][j][m][i][r].attrib['language']
                                    coder=''
                                    if 'coder' in (root[x][j][m][i][r].attrib):
                                        coder=root[x][j][m][i][r].attrib['language']
                                    synonym=root[x][j][m][i][r].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_transporter_poly_synonyms select '"+primary_id+"','"+transporter_id+"','"+str(r+1)+"','"+poly_id+"','"+lan+"','"+coder+"','"+synonym+"' where not exists(select drug_id from drug_transporter_poly_synonyms where drug_id='"+primary_id+"' and counter='"+str(r+1)+"' and polypeptide_id='"+poly_id+"' and transporter_id='"+transporter_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_transporter_poly_ex_iden_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='external-identifiers':
                                for r in range(0,len(root[x][j][m][i])):
                                    rsc=root[x][j][m][i][r][0].text
                                    identifier=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_transporter_poly_ex_iden select '"+primary_id+"','"+transporter_id+"','"+poly_id+"','"+str(r+1)+"','"+rsc+"','"+identifier+"' where not exists(select drug_id from drug_transporter_poly_ex_iden where drug_id='"+primary_id+"' and counter='"+str(r+1)+"' and polypeptide_id='"+poly_id+"' and transporter_id='"+transporter_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_transporter_poly_aminoacid_seq_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='amino-acid-sequence':
                                seq=root[x][j][m][i].text
                                frm=''
                                if 'format' in (root[x][j][m][i].attrib):
                                    frm=root[x][j][m][i].attrib['format']
                                qry = "set nocount off set ansi_warnings off insert into  drug_transporter_poly_aminoacid_seq select '"+primary_id+"','"+transporter_id+"','"+poly_id+"','"+frm+"','"+seq+"' where not exists(select drug_id from drug_transporter_poly_aminoacid_seq where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and transporter_id='"+transporter_id+"')"
                                cur.execute(qry)
                                con.commit()

def drug_transporter_poly_gene_seq_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='gene-sequence':
                                seq=root[x][j][m][i].text
                                frm=''
                                if 'format' in (root[x][j][m][i].attrib):
                                    frm=root[x][j][m][i].attrib['format']
                                qry = "set nocount off set ansi_warnings off insert into  drug_transporter_poly_gene_seq select '"+primary_id+"','"+transporter_id+"','"+poly_id+"','"+frm+"','"+seq+"' where not exists(select drug_id from drug_transporter_poly_gene_seq where drug_id='"+primary_id+"' and polypeptide_id='"+poly_id+"' and transporter_id='"+transporter_id+"')"
                                cur.execute(qry)
                                con.commit()

def drug_transporter_poly_pfams_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='pfams':
                                for r in range(0,len(root[x][j][m][i])):
                                    pfam_identifier=root[x][j][m][i][r][0].text
                                    pfam_name=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_transporter_poly_pfams select '"+primary_id+"','"+transporter_id+"','"+poly_id+"','"+pfam_name+"','"+pfam_identifier+"' where not exists(select drug_id from drug_transporter_poly_pfams where drug_id='"+primary_id+"' and identifier='"+pfam_identifier+"' and polypeptide_id='"+poly_id+"' and transporter_id='"+transporter_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def drug_transporter_poly_go_classifier_ins():
    inx=0
    while ('primary' not in root[inx].attrib):
        inx=inx+1
    primary_id=root[inx].text
    for x in range(0,len(root)):
        if root[x].tag=='transporters':
            for j in range(0,len(root[x])):
                transporter_id=root[x][j][0].text
                for m in range(0,len(root[x][j])):
                    if root[x][j][m].tag=='polypeptide':
                        poly_id=root[x][j][m].attrib['id']
                        for i in range(0,len(root[x][j][m])):
                            if root[x][j][m][i].tag=='go-classifiers':
                                for r in range(0,len(root[x][j][m][i])):
                                    category=root[x][j][m][i][r][0].text
                                    description=root[x][j][m][i][r][1].text
                                    qry = "set nocount off set ansi_warnings off insert into  drug_transporter_poly_go_classfier select '"+primary_id+"','"+transporter_id+"','"+poly_id+"','"+category+"','"+description+"' where not exists(select drug_id from drug_transporter_poly_go_classfier where drug_id='"+primary_id+"' and category='"+category+"' and classifier_description='"+description+"' and polypeptide_id='"+poly_id+"' and transporter_id='"+transporter_id+"')"
                                    cur.execute(qry)
                                    con.commit()

def begin_insert(low_index):
    high_index=low_index+step
    if high_index>number_of_drugs:
        high_index=number_of_drugs+1
    for i in range(low_index,high_index):
        print(str(i)+" th drug is proccesing")
        import xml.etree.ElementTree as ET
        tree = ET.parse('drugs/'+str(i)+'.xml')
        global root
        root = tree.getroot()
        drug_ins()
        drug_second_id_ins()
        drug_groups_ins()
        drug_reference_article_ins()
        drug_reference_text_book_ins()
        drug_reference_text_link_ins()
        drugs_properties_ins()
        drug_classification_ins()
        drug_salt_ins()
        drug_synonyms_ins()
        drug_product_ins()
        drug_brand_ins()
        drug_mixture_ins()
        drug_packager_ins()
        drug_manufactors_ins()
        drug_price_ins()
        drug_category_ins()
        drug_affected_organism_ins()
        drug_dosage_ins()
        drug_atc_code_ins()
        drug_ahfs_code_ins()
        drug_pdb_entries_ins()
        drug_patent_ins()
        drug_food_interaction_ins()
        drug_interaction_ins()
        drug_sequence_ins()
        drug_experimental_properties_ins()
        drug_calculated_properties_ins()
        drug_external_identifiers_ins()
        drug_external_links_ins()
        drug_pathways_ins()
        drug_reaction_ins()
        drug_snp_effects_ins()
        drug_snp_adverse_reaction_ins()
        drug_targets_ins()
        drug_targets_actions_ins()
        drug_target_reference_article_ins()
        drug_target_reference_text_book_ins()
        drug_target_reference_text_link_ins()
        drug_targets_polypeptide_ins()
        drug_target_poly_ex_iden_ins()
        drug_target_poly_synonyms_ins()
        drug_target_poly_aminoacid_seq_ins()
        drug_target_poly_gene_seq_ins()
        drug_target_poly_pfams_ins()
        drug_target_poly_go_classifier_ins()
        drug_enzymes_ins()
        drug_enzymes_actions_ins()
        drug_enzyme_reference_article_ins()
        drug_enzyme_reference_text_book_ins()
        drug_enzyme_reference_text_link_ins()
        drug_enzymes_polypeptide_ins()
        drug_enzyme_poly_ex_iden_ins()
        drug_enzyme_poly_synonyms_ins()
        drug_enzyme_poly_aminoacid_seq_ins()
        drug_enzyme_poly_gene_seq_ins()
        drug_enzyme_poly_pfams_ins()
        drug_enzyme_poly_go_classifier_ins()
        drug_carriers_ins()
        drug_carriers_actions_ins()
        drug_carrier_reference_article_ins()
        drug_carrier_reference_text_book_ins()
        drug_carrier_reference_text_link_ins()
        drug_carriers_polypeptide_ins()
        drug_carrier_poly_ex_iden_ins()
        drug_carrier_poly_synonyms_ins()
        drug_carrier_poly_aminoacid_seq_ins()
        drug_carrier_poly_gene_seq_ins()
        drug_carrier_poly_pfams_ins()
        drug_carrier_poly_go_classifier_ins()
        drug_transporters_ins()
        drug_transporters_actions_ins()
        drug_transporter_reference_article_ins()
        drug_transporter_reference_text_book_ins()
        drug_transporter_reference_text_link_ins()
        drug_transporters_polypeptide_ins()
        drug_transporter_poly_ex_iden_ins()
        drug_transporter_poly_synonyms_ins()
        drug_transporter_poly_aminoacid_seq_ins()
        drug_transporter_poly_gene_seq_ins()
        drug_transporter_poly_pfams_ins()
        drug_transporter_poly_go_classifier_ins()
    con.close()
    print("The operations completed succefully")

import pyodbc as db
db_name="DrugR"
server_name="."
con = db.connect('DATABASE='+db_name+';SERVER='+server_name+';Driver=Sql server')
cur = con.cursor()
number_of_drugs=11292
step=22
i=1
data_index_list=[]
while i<number_of_drugs:
    data_index_list.append(i)
    i=i+step
print("Multi processing executions were started. Please wait")
from multiprocessing import Pool
if __name__ == '__main__':
    p = Pool(526)
    p.map(begin_insert,data_index_list)
