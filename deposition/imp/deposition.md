# Deposition of IMP models

All published models should be listed on the
[IMP website](https://integrativemodeling.org/systems/). Some of these may
be suitable for deposition once issues (below) are resolved.

## [40S•eIF1•eIF3 Complex](https://salilab.org/40S-eIF1-eIF3)

 - No obvious barriers to deposition.
 - The EM maps used in this study were not used as restraints, but only for
   assessment (see [figure S6](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4151992/figure/figs6/)).
 - Category list
    - `entity`, `entity_poly`                   Manual
    - `entity_poly_seq`, `struct_asym`          Github (fasta sequences) and manual
    - `ihm_model_representation`                Supplementary figure S7
    - `ihm_struct_assembly`                     Manual
    - `ihm_dataset_list`                        Manual (Crosslinks, 3DEM map used for validation only)
    - `ihm_dataset_related_db_reference`        Manual
    - `ihm_dataset_other`                       Manual
    - `ihm_starting_model_details`              Supplementary methods section in the paper
    - `ihm_starting_model_coord`                Github
    - `ihm_cross_link_list`                     Github
    - `ihm_cross_link_restraint`                Github (psi and sigma values may come from IMP)
    - `ihm_cross_link_result`                   Supplementary material
    - `ihm_3dem_restraint`                      Publication, Figure 3 (used for validation only)
    - `ihm_2dem_restraint`                      n/a
    - `ihm_2dem_fitting`                        n/a
    - `ihm_modeling_protocol`                   Figure S6, supplementary material
    - `ihm_multi_state_modeling`                n/a
    - `ihm_time_ordered_ensemble`               n/a
    - `ihm_modeling_post_process`               Figure S6, supplementary material
    - `ihm_ensemble_info`                       Supplementary material
    - `ihm_model_list`                          Manual
    - `atom_site`                               IMP
    - `ihm_sphere_obj_site`                     IMP
    - `ihm_gaussian_obj_site`                   n/a
    - `ihm_gaussian_obj_ensemble`               Github and supplementary figure S8
    - `author`, `software`, `citation`          Github and manual

## [Exosome modeling](https://salilab.org/exosome)

 - No obvious barriers to deposition.

 - Category list
    - `entity`, `entity_poly`                   Manual
    - `entity_poly_seq`, `struct_asym`          Github (fasta sequences) & Manual
    - `ihm_model_representation`                Supplementary figure, S12 (may require raw data)
    - `ihm_struct_assembly`                     Manual
    - `ihm_dataset_list`                        Manual (Crosslinks)
    - `ihm_dataset_related_db_reference`        Manual
    - `ihm_dataset_other`                       Manual
    - `ihm_starting_model_details`              Methods section in the paper
    - `ihm_starting_model_coord`                Github 
    - `ihm_cross_link_list`                     Github
    - `ihm_cross_link_restraint`                Github (psi and sigma values from IMP)
    - `ihm_cross_link_result`                   Supplementary figure, S14 (may require raw data) and Github
    - `ihm_3dem_restraint`                      n/a
    - `ihm_2dem_restraint`                      n/a
    - `ihm_2dem_fitting`                        n/a
    - `ihm_modeling_protocol`                   Methods section in the paper
    - `ihm_multi_state_modeling`                n/a
    - `ihm_time_ordered_ensemble`               n/a
    - `ihm_modeling_post_process`               Methods section in the paper
    - `ihm_ensemble_info`                       Github and methods section in the paper (clusters and cluster precisions)
    - `ihm_model_list`                          Manual
    - `atom_site`                               IMP
    - `ihm_sphere_obj_site`                     IMP
    - `ihm_gaussian_obj_site`                   n/a
    - `ihm_gaussian_obj_ensemble`               Figure 2 (i and j) in the paper (may require raw data)
    - `author`, `software`, `citation`          Github and manual

## [Nup84 Complex](https://salilab.org/nup84)

 - Need [localization density maps](https://github.com/integrativemodeling/nup84/issues/2).

 - Category list
    - `entity`, `entity_poly`                   Manual
    - `entity_poly_seq`, `struct_asym`          Github (fasta sequences) & Manual
    - `ihm_model_representation`                Supplementary figure S3 (may need raw data)
    - `ihm_struct_assembly`                     Manual
    - `ihm_dataset_list`                        Manual (Crosslinks and 2DEM class averages, 3DEM map used for validation only)
    - `ihm_dataset_related_db_reference`        Manual
    - `ihm_dataset_other`                       Manual
    - `ihm_starting_model_details`              Supplementary figure S3
    - `ihm_starting_model_coord`                Github
    - `ihm_cross_link_list`                     Github
    - `ihm_cross_link_restraint`                Github (psi and sigma values from IMP)
    - `ihm_cross_link_result`                   Supplementary figure S4 (may need raw data)
    - `ihm_3dem_restraint`                      Negative stain 3DEM used for validation (Supplementary figure S8)
    - `ihm_2dem_restraint`                      Github
    - `ihm_2dem_fitting`                        Cross-correlation coefficient available in the paper. 
                                                Transformation matrix not available
    - `ihm_modeling_protocol`                   Figure 4, methods section of paper
    - `ihm_multi_state_modeling`                n/a
    - `ihm_time_ordered_ensemble`               n/a
    - `ihm_modeling_post_process`               Figure 4, methods section of paper
    - `ihm_ensemble_info`                       Supplementary tables S4 & S5, Figure 4 in main paper
    - `ihm_model_list`                          Manual
    - `atom_site`                               IMP
    - `ihm_sphere_obj_site`                     IMP
    - `ihm_gaussian_obj_site`                   n/a
    - `ihm_gaussian_obj_ensemble`               Supplementary figures S6 & S7 (may need raw data)
    - `author`, `software`, `citation`          Github and manual

## [PDE6](https://salilab.org/pde6)

 - PMI was not used, so more manual work will be necessary to extract all of
   the data needed for the mmCIF files.

 - Category list
    - `entity`, `entity_poly`                   Manual
    - `entity_poly_seq`, `struct_asym`          Manual (no fasta sequence on Github)
    - `ihm_model_representation`                Methods section of paper (all atom models generated from coarse-grained models)
    - `ihm_struct_assembly`                     Manual
    - `ihm_dataset_list`                        Manual (Crosslinks and 3DEM map)
    - `ihm_dataset_related_db_reference`        Manual
    - `ihm_dataset_other`                       Manual
    - `ihm_starting_model_details`              Methods section of paper
    - `ihm_starting_model_coord`                Github
    - `ihm_cross_link_list`                     Tables 1, 2 & 3 in the paper (not available on Github)
    - `ihm_cross_link_restraint`                Tables 1, 2 & 3 (psi and sigma values missing)
    - `ihm_cross_link_result`                   May be supplementary material Table 2 / not available
    - `ihm_3dem_restraint`                      Github (meta data??)
    - `ihm_2dem_restraint`                      n/a
    - `ihm_2dem_fitting`                        n/a
    - `ihm_modeling_protocol`                   Methods section of paper
    - `ihm_multi_state_modeling`                n/a
    - `ihm_time_ordered_ensemble`               n/a
    - `ihm_modeling_post_process`               Methods section of paper
    - `ihm_ensemble_info`                       Not available
    - `ihm_model_list`                          Manual
    - `atom_site`                               IMP
    - `ihm_sphere_obj_site`                     IMP
    - `ihm_gaussian_obj_site`                   n/a
    - `ihm_gaussian_obj_ensemble`               Not available
    - `author`, `software`, `citation`          Github and manual

## [PhoQ](https://salilab.org/phoq)

 - PMI was not used, so more manual work will be necessary to extract all of
   the data needed for the mmCIF files.

 - Category list
    - `entity`, `entity_poly`                   Manual 
    - `entity_poly_seq`, `struct_asym`          Manual (no fasta sequence on Github)
    - `ihm_model_representation`                Methods section in paper
    - `ihm_struct_assembly`                     Manual
    - `ihm_dataset_list`                        Manual (Cysteine crosslinks)
    - `ihm_dataset_related_db_reference`        Manual
    - `ihm_dataset_other`                       Manual
    - `ihm_starting_model_details`              Methods section and figure 1 in paper
    - `ihm_starting_model_coord`                Github
    - `ihm_cross_link_list`                     Github (phoq/modeling/data/expcrosslink-full.dat, phoq/modeling/2Y20-MC-2-FULL-90-PERCENT-DATA-1/expcrosslink-90-percent.dat and others)
    - `ihm_cross_link_restraint`                Github (psi and sigma values are missing)
    - `ihm_cross_link_result`                   Not available
    - `ihm_3dem_restraint`                      n/a
    - `ihm_2dem_restraint`                      n/a
    - `ihm_2dem_fitting`                        n/a
    - `ihm_modeling_protocol`                   From the paper
    - `ihm_multi_state_modeling`                From the paper
    - `ihm_time_ordered_ensemble`               n/a
    - `ihm_modeling_post_process`               From the paper
    - `ihm_ensemble_info`                       Data-based clustering (raw data not available, refer to supplementary table S1)
    - `ihm_model_list`                          Manual
    - `atom_site`                               IMP
    - `ihm_sphere_obj_site`                     IMP
    - `ihm_gaussian_obj_site`                   n/a
    - `ihm_gaussian_obj_ensemble`               Github (what are .dx files?)
    - `author`, `software`, `citation`          Github and manual

 - Refer to supplementary methods for data-based clustering and multi-state modeling.

## [Mediator](https://salilab.org/mediator/)

 - An older version of PMI was used; needs work to clean up and adapt to
   modern PMI.

 - Category list
    - `entity`, `entity_poly`                   Manual
    - `entity_poly_seq`, `struct_asym`          Manual and Github (fasta sequences)
    - `ihm_model_representation`                From the paper
    - `ihm_struct_assembly`                     Manual
    - `ihm_dataset_list`                        Manual (Crosslinks and EM map)
    - `ihm_dataset_related_db_reference`        Manual
    - `ihm_dataset_other`                       Manual
    - `ihm_starting_model_details`              From the paper
    - `ihm_starting_model_coord`                Github
    - `ihm_cross_link_list`                     Github (in a format different from the usual)
    - `ihm_cross_link_restraint`                Github (psi and sigma values not available)
    - `ihm_cross_link_result`                   Crosslinks maps available on Github (raw data required)
    - `ihm_3dem_restraint`                      Github and the paper (EM map has been segmented)
    - `ihm_2dem_restraint`                      n/a
    - `ihm_2dem_fitting`                        n/a
    - `ihm_modeling_protocol`                   From the paper
    - `ihm_multi_state_modeling`                n/a
    - `ihm_time_ordered_ensemble`               n/a
    - `ihm_modeling_post_process`               From the paper
    - `ihm_ensemble_info`                       Github and the paper (clusters and cluster precisions)
    - `ihm_model_list`                          Manual
    - `atom_site`                               IMP
    - `ihm_sphere_obj_site`                     IMP
    - `ihm_gaussian_obj_site`                   n/a
    - `ihm_gaussian_obj_ensemble`               Github (in mrc and gmm formats)
    - `author`, `software`, `citation`          Github and Manual (citation missing on Github)
 - Note: The readme file on Github has a lot of information on the files/data available. EM map has been segmented. 

## [Nup133](https://salilab.org/nup133)

 - Need to chase up the authors and get them to deposit scripts,
   outputs, etc.

 - SAXS data needs to be submitted to SASBDB. All metadata and SAS-related definitions are captured in the 
   [SAS dictionary](http://mmcif.wwpdb.org/dictionaries/mmcif_sas.dic/Index/). 

 - Category list
    - `entity`, `entity_poly`                   Manual
    - `entity_poly_seq`, `struct_asym`          Manual (no fasta sequence on Github)
    - `ihm_model_representation`                Not sure if it is single-scale (all atomistic)
    - `ihm_struct_assembly`                     Manual
    - `ihm_dataset_list`                        Manual (Crosslinks, 2DEM and SAXS)
    - `ihm_dataset_related_db_reference`        Manual
    - `ihm_dataset_other`                       Manual
    - `ihm_starting_model_details`              From the paper
    - `ihm_starting_model_coord`                Github
    - `ihm_cross_link_list`                     Github (DSS and EDC crosslinks in a different format than usual) 
                                                Refer to tables 2 & 3 in the paper
    - `ihm_cross_link_restraint`                Github (psi and sigma values are missing)
    - `ihm_cross_link_result`                   Tables 2 & 3 in the paper
    - `ihm_3dem_restraint`                      n/a
    - `ihm_2dem_restraint`                      Github (multiple class average images as .hdf files)
                                                Refer to supplemetary table S3 for metadata, figure 3 in the paper
    - `ihm_2dem_fitting`                        Cross-correlation coefficients in Table S3, supplementary material
                                                Transformation matrix not available
    - `ihm_modeling_protocol`                   From the paper (methods section and Figure 1)
    - `ihm_multi_state_modeling`                4 states from the paper (1 major extended and 2 minor compact states)
    - `ihm_time_ordered_ensemble`               n/a
    - `ihm_modeling_post_process`               From the paper (methods section and Figure 1)
    - `ihm_ensemble_info`                       Minimal cluster information available in the paper
    - `ihm_model_list`                          Manual
    - `atom_site`                               IMP
    - `ihm_sphere_obj_site`                     IMP
    - `ihm_gaussian_obj_site`                   n/a
    - `ihm_gaussian_obj_ensemble`               Not available
    - `author`, `software`, `citation`          Github & Manual
 - 23 2DEM class averages and 19 SAXS profiles were used. 18 DSS and 23 EDC intra-molecular crosslinks within Nup133 
   and 2 DSS and 2 EDC inter-molecular crosslinks between Nup133 and Nup84 were used. 

## [SEA complex](https://salilab.org/sea)

 - Need to chase up the authors and get them to deposit scripts,
   outputs, etc.

 - Category list
    - `entity`, `entity_poly`                   Manual
    - `entity_poly_seq`, `struct_asym`          Manual (no fasta sequence on Github)
    - `ihm_model_representation`                From the paper (supplementary figure S3 and table S5)
    - `ihm_struct_assembly`                     Manual
    - `ihm_dataset_list`                        Manual (Crosslinks)
    - `ihm_dataset_related_db_reference`        Manual
    - `ihm_dataset_other`                       Manual
    - `ihm_starting_model_details`              From the paper (methods section)
    - `ihm_starting_model_coord`                Github
    - `ihm_cross_link_list`                     Github and supplementary table S4
    - `ihm_cross_link_restraint`                Github (psi and sigma values missing)
    - `ihm_cross_link_result`                   Supplementary table S8, figures S5 & S6 and Figure 3 in the paper
    - `ihm_3dem_restraint`                      n/a
    - `ihm_2dem_restraint`                      n/a
    - `ihm_2dem_fitting`                        n/a
    - `ihm_modeling_protocol`                   From the paper (methods section and Figure 2)
    - `ihm_multi_state_modeling`                n/a
    - `ihm_time_ordered_ensemble`               n/a
    - `ihm_modeling_post_process`               From the paper (methods section and Figure 2)
    - `ihm_ensemble_info`                       Cluster and precision information available in the paper (methods section)
                                                Supplementary figure S4
    - `ihm_model_list`                          Manual
    - `atom_site`                               IMP
    - `ihm_sphere_obj_site`                     IMP
    - `ihm_gaussian_obj_site`                   n/a
    - `ihm_gaussian_obj_ensemble`               Figures 2 & 3 from the paper (raw data is required)
    - `author`, `software`, `citation`          Github & Manual

## [TFIIH complex](https://salilab.org/tfiih)

 - An older version of PMI was used; needs work to clean up and adapt to
   modern PMI.
 
 - Two separate modeling experiments are carried out, one for yeast TFIIH complex and another for the human counterpart. 

 - Category list
    - `entity`, `entity_poly`                   Manual
    - `entity_poly_seq`, `struct_asym`          Manual (no fasta sequence on Github)
    - `ihm_model_representation`                From the paper (methods section and supplementary figure S4)
    - `ihm_struct_assembly`                     Manual 
    - `ihm_dataset_list`                        Manual (Crosslinks and 3DEM map)
    - `ihm_dataset_related_db_reference`        Manual
    - `ihm_dataset_other`                       Manual
    - `ihm_starting_model_details`              Supplementary table S5
    - `ihm_starting_model_coord`                Github
    - `ihm_cross_link_list`                     Github and supplementary table S1
    - `ihm_cross_link_restraint`                Github (psi and sigma values are missing)
    - `ihm_cross_link_result`                   Supplementary figure S5 and table S6
    - `ihm_3dem_restraint`                      3DEM map in mrc format is available on Github (metadata?)
    - `ihm_2dem_restraint`                      n/a
    - `ihm_2dem_fitting`                        n/a
    - `ihm_modeling_protocol`                   From the paper (methods section and supplementary figure S3)
    - `ihm_multi_state_modeling`                n/a
    - `ihm_time_ordered_ensemble`               n/a
    - `ihm_modeling_post_process`               From the paper (methods section and supplementary figure S3)
    - `ihm_ensemble_info`                       Supplementary figures S3, S4 and supplementary methods
    - `ihm_model_list`                          Manual
    - `atom_site`                               IMP
    - `ihm_sphere_obj_site`                     IMP
    - `ihm_gaussian_obj_site`                   n/a
    - `ihm_gaussian_obj_ensemble`               Figure 2 in the paper and supplementary figures S3 and S4 (raw data is required)
    - `author`, `software`, `citation`          Github & Manual

 - Note: Refer to details in the supplementary methods, figures and tables. 

#### What about elF3, GroEL, Integrin and Glycophorin modeling available on IMP website?
