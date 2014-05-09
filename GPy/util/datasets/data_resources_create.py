import json

neil_url = 'http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/dataset_mirror/'
sam_url = 'http://www.cs.nyu.edu/~roweis/data/'
cmu_url = 'http://mocap.cs.cmu.edu/subjects/'

data_resources = {'ankur_pose_data' : {'urls' : [neil_url + 'ankur_pose_data/'],
                                       'files' : [['ankurDataPoseSilhouette.mat']],
                                       'license' : None,
                                       'citation' : """3D Human Pose from Silhouettes by Relevance Vector Regression (In CVPR'04). A. Agarwal and B. Triggs.""",
                                       'details' : """Artificially generated data of silhouettes given poses. Note that the data does not display a left/right ambiguity because across the entire data set one of the arms sticks out more the the other, disambiguating the pose as to which way the individual is facing."""},

                  'boston_housing' : {'urls' : ['http://archive.ics.uci.edu/ml/machine-learning-databases/housing/'],
                                      'files' : [['Index', 'housing.data', 'housing.names']],
                                      'citation' : """Harrison, D. and Rubinfeld, D.L. 'Hedonic prices and the demand for clean air', J. Environ. Economics & Management, vol.5, 81-102, 1978.""",
                                      'details' : """The Boston Housing data relates house values in Boston to a range of input variables.""",
                                      'license' : None,
                                      'size' : 51276
                                      },
                  'brendan_faces' : {'urls' : [sam_url],
                                     'files': [['frey_rawface.mat']],
                                     'citation' : 'Frey, B. J., Colmenarez, A and Huang, T. S. Mixtures of Local Linear Subspaces for Face Recognition. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition 1998, 32-37, June 1998. Computer Society Press, Los Alamitos, CA.',
                                     'details' : """A video of Brendan Frey's face popularized as a benchmark for visualization by the Locally Linear Embedding.""",
                                     'license': None,
                                     'size' : 1100584},
                  'cmu_mocap_full' : {'urls' : ['http://mocap.cs.cmu.edu'],
                                      'files' : [['allasfamc.zip']],
                                      'citation' : """Please include this in your acknowledgements: The data used in this project was obtained from mocap.cs.cmu.edu.'
                                      'The database was created with funding from NSF EIA-0196217.""",
                                      'details' : """CMU Motion Capture data base. Captured by a Vicon motion capture system consisting of 12 infrared MX-40 cameras, each of which is capable of recording at 120 Hz with images of 4 megapixel resolution. Motions are captured in a working volume of approximately 3m x 8m. The capture subject wears 41 markers and a stylish black garment.""",
                                      'license' : """From http://mocap.cs.cmu.edu. This data is free for use in research projects. You may include this data in commercially-sold products, but you may not resell this data directly, even in converted form. If you publish results obtained using this data, we would appreciate it if you would send the citation to your published paper to jkh+mocap@cs.cmu.edu, and also would add this text to your acknowledgments section: The data used in this project was obtained from mocap.cs.cmu.edu. The database was created with funding from NSF EIA-0196217.""",
                                      'size' : None},
                  'creep_rupture' : {'urls' : ['http://www.msm.cam.ac.uk/map/data/tar/'],
                                     'files' : [['creeprupt.tar']],
                                     'citation' : 'Materials Algorithms Project Data Library: MAP_DATA_CREEP_RUPTURE. F. Brun and T. Yoshida.',
                                     'details' : """Provides 2066 creep rupture test results of steels (mainly of two kinds of steels: 2.25Cr and 9-12 wt% Cr ferritic steels). See http://www.msm.cam.ac.uk/map/data/materials/creeprupt-b.html.""",
                                     'license' : None,
                                     'size' : 602797},
                  'della_gatta' : {'urls' : [neil_url + 'della_gatta/'],
                                   'files': [['DellaGattadata.mat']],
                                   'citation' : 'Direct targets of the TRP63 transcription factor revealed by a combination of gene expression profiling and reverse engineering. Giusy Della Gatta, Mukesh Bansal, Alberto Ambesi-Impiombato, Dario Antonini, Caterina Missero, and Diego di Bernardo, Genome Research 2008',
                                   'details': "The full gene expression data set from della Gatta et al (http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2413161/) processed by RMA.",
                                   'license':None,
                                   'size':3729650},
                  'epomeo_gpx' : {'urls' : [neil_url + 'epomeo_gpx/'],
                                   'files': [['endomondo_1.gpx', 'endomondo_2.gpx', 'garmin_watch_via_endomondo.gpx','viewranger_phone.gpx','viewranger_tablet.gpx']],
                                   'citation' : '',
                                   'details': "Five different GPS traces of the same run up Mount Epomeo in Ischia. The traces are from different sources. endomondo_1 and endomondo_2 are traces from the mobile phone app Endomondo, with a split in the middle. garmin_watch_via_endomondo is the trace from a Garmin watch, with a segment missing about 4 kilometers in. viewranger_phone and viewranger_tablet are traces from a phone and a tablet through the viewranger app. The viewranger_phone data comes from the same mobile phone as the Endomondo data (i.e. there are 3 GPS devices, but one device recorded two traces).",
                                   'license':None,
                                   'size': 2031872},
                  'three_phase_oil_flow': {'urls' : [neil_url + 'three_phase_oil_flow/'],
                                           'files' : [['DataTrnLbls.txt', 'DataTrn.txt', 'DataTst.txt', 'DataTstLbls.txt', 'DataVdn.txt', 'DataVdnLbls.txt']],
                                           'citation' : 'Bishop, C. M. and G. D. James (1993). Analysis of multiphase flows using dual-energy gamma densitometry and neural networks. Nuclear Instruments and Methods in Physics Research A327, 580-593',
                                           'details' : """The three phase oil data used initially for demonstrating the Generative Topographic mapping.""",
                                           'license' : None,
                                           'size' : 712796},
                  'rogers_girolami_data' : {'urls' : ['https://www.dropbox.com/sh/7p6tu1t29idgliq/_XqlH_3nt9/'],
                                            'files' : [['firstcoursemldata.tar.gz']],
                                            'suffices' : [['?dl=1']],
                                            'citation' : 'A First Course in Machine Learning. Simon Rogers and Mark Girolami: Chapman & Hall/CRC, ISBN-13: 978-1439824146',
                                            'details' : """Data from the textbook 'A First Course in Machine Learning'. Available from http://www.dcs.gla.ac.uk/~srogers/firstcourseml/.""",
                                            'license' : None,
                                            'size' : 21949154},
                  'olivetti_faces' : {'urls' : [neil_url + 'olivetti_faces/', sam_url],
                                      'files' : [['att_faces.zip'], ['olivettifaces.mat']],
                                            'citation' : 'Ferdinando Samaria and Andy Harter, Parameterisation of a Stochastic Model for Human Face Identification. Proceedings of 2nd IEEE Workshop on Applications of Computer Vision, Sarasota FL, December 1994',
                                            'details' : """Olivetti Research Labs Face data base, acquired between December 1992 and December 1994 in the Olivetti Research Lab, Cambridge (which later became AT&T Laboratories, Cambridge). When using these images please give credit to AT&T Laboratories, Cambridge. """,
                                            'license': None,
                                            'size' : 8561331},
                  'olympic_marathon_men' : {'urls' : [neil_url + 'olympic_marathon_men/'],
                                            'files' : [['olympicMarathonTimes.csv']],
                                            'citation' : None,
                                            'details' : """Olympic mens' marathon gold medal winning times from 1896 to 2012. Time given in pace (minutes per kilometer). Data is originally downloaded and collated from Wikipedia, we are not responsible for errors in the data""",
                                            'license': None,
                                            'size' : 584},
                  'osu_run1' : {'urls': ['http://accad.osu.edu/research/mocap/data/', neil_url + 'stick/'],
                                'files': [['run1TXT.ZIP'],['connections.txt']],
                                'details' : "Motion capture data of a stick man running from the Open Motion Data Project at Ohio State University.",
                                'citation' : 'The Open Motion Data Project by The Ohio State University Advanced Computing Center for the Arts and Design, http://accad.osu.edu/research/mocap/mocap_data.htm.',
                                'license' : 'Data is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License (http://creativecommons.org/licenses/by-nc-sa/3.0/).',
                                'size': 338103},
                  'osu_accad' : {'urls': ['http://accad.osu.edu/research/mocap/data/', neil_url + 'stick/'],
                                'files': [['swagger1TXT.ZIP','handspring1TXT.ZIP','quickwalkTXT.ZIP','run1TXT.ZIP','sprintTXT.ZIP','dogwalkTXT.ZIP','camper_04TXT.ZIP','dance_KB3_TXT.ZIP','per20_TXT.ZIP','perTWO07_TXT.ZIP','perTWO13_TXT.ZIP','perTWO14_TXT.ZIP','perTWO15_TXT.ZIP','perTWO16_TXT.ZIP'],['connections.txt']],
                                'details' : "Motion capture data of different motions from the Open Motion Data Project at Ohio State University.",
                                'citation' : 'The Open Motion Data Project by The Ohio State University Advanced Computing Center for the Arts and Design, http://accad.osu.edu/research/mocap/mocap_data.htm.',
                                'license' : 'Data is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License (http://creativecommons.org/licenses/by-nc-sa/3.0/).',
                                'size': 15922790},
                  'pumadyn-32nm' : {'urls' : ['ftp://ftp.cs.toronto.edu/pub/neuron/delve/data/tarfiles/pumadyn-family/'],
                                    'files' : [['pumadyn-32nm.tar.gz']],
                                    'details' : """Pumadyn non linear 32 input data set with moderate noise. See http://www.cs.utoronto.ca/~delve/data/pumadyn/desc.html for details.""",
                                    'citation' : """Created by Zoubin Ghahramani using the Matlab Robotics Toolbox of Peter Corke. Corke, P. I. (1996). A Robotics Toolbox for MATLAB. IEEE Robotics and Automation Magazine, 3 (1): 24-32.""",
                                    'license' : """Data is made available by the Delve system at the University of Toronto""",
                                    'size' : 5861646},
                  'robot_wireless' : {'urls' : [neil_url + 'robot_wireless/'],
                                      'files' : [['uw-floor.txt']],
                                      'citation' : """WiFi-SLAM using Gaussian Process Latent Variable Models by Brian Ferris, Dieter Fox and Neil Lawrence in IJCAI'07 Proceedings pages 2480-2485. Data used in A Unifying Probabilistic Perspective for Spectral Dimensionality Reduction: Insights and New Models by Neil D. Lawrence, JMLR 13 pg 1609--1638, 2012.""",
                                      'details' : """Data created by Brian Ferris and Dieter Fox. Consists of WiFi access point strengths taken during a circuit of the Paul Allen building at the University of Washington.""",
                                      'license' : None,
                                      'size' : 284390},
                  'swiss_roll' : {'urls' : ['http://isomap.stanford.edu/'],
                                  'files' : [['swiss_roll_data.mat']],
                                  'details' : """Swiss roll data made available by Tenenbaum, de Silva and Langford to demonstrate isomap, available from http://isomap.stanford.edu/datasets.html.""",
                                  'citation' : 'A Global Geometric Framework for Nonlinear Dimensionality Reduction, J. B. Tenenbaum, V. de Silva and J. C. Langford, Science 290 (5500): 2319-2323, 22 December 2000',
                                  'license' : None,
                                  'size' : 800256},
                  'ripley_prnn_data' : {'urls' : ['http://www.stats.ox.ac.uk/pub/PRNN/'],
                                        'files' : [['Cushings.dat', 'README', 'crabs.dat', 'fglass.dat', 'fglass.grp', 'pima.te', 'pima.tr', 'pima.tr2', 'synth.te', 'synth.tr', 'viruses.dat', 'virus3.dat']],
                                        'details' : """Data sets from Brian Ripley's Pattern Recognition and Neural Networks""",
                                        'citation': """Pattern Recognition and Neural Networks by B.D. Ripley (1996) Cambridge University Press ISBN 0 521 46986 7""",
                                        'license' : None,
                                        'size' : 93565},
                  'isomap_face_data' : {'urls' : [neil_url + 'isomap_face_data/'],
                                        'files' : [['face_data.mat']],
                                        'details' : """Face data made available by Tenenbaum, de Silva and Langford to demonstrate isomap, available from http://isomap.stanford.edu/datasets.html.""",
                                        'citation' : 'A Global Geometric Framework for Nonlinear Dimensionality Reduction, J. B. Tenenbaum, V. de Silva and J. C. Langford, Science 290 (5500): 2319-2323, 22 December 2000',
                                        'license' : None,
                                        'size' : 24229368},
                  'xw_pen' : {'urls' : [neil_url + 'xw_pen/'],
                                        'files' : [['xw_pen_15.csv']],
                                        'details' : """Accelerometer pen data used for robust regression by Tipping and Lawrence.""",
                                        'citation' : 'Michael E. Tipping and Neil D. Lawrence. Variational inference for Student-t models: Robust Bayesian interpolation and generalised component analysis. Neurocomputing, 69:123--141, 2005',
                                        'license' : None,
                                        'size' : 3410},
                  'hapmap3' : {'urls' : ['http://hapmap.ncbi.nlm.nih.gov/downloads/genotypes/latest_phaseIII_ncbi_b36/plink_format/'],
                                 'files' : [['hapmap3_r2_b36_fwd.consensus.qc.poly.map.bz2', 'hapmap3_r2_b36_fwd.consensus.qc.poly.ped.bz2', 'relationships_w_pops_121708.txt']],
                                 'details' : """
        HapMap Project: Single Nucleotide Polymorphism sequenced in all human populations. 
        The HapMap phase three SNP dataset - 1184 samples out of 11 populations.
        See http://www.nature.com/nature/journal/v426/n6968/abs/nature02168.html for details.

        SNP_matrix (A) encoding [see Paschou et all. 2007 (PCA-Correlated SNPs...)]:
        Let (B1,B2) be the alphabetically sorted bases, which occur in the j-th SNP, then

              /  1, iff SNPij==(B1,B1)
        Aij = |  0, iff SNPij==(B1,B2)
              \ -1, iff SNPij==(B2,B2)

        The SNP data and the meta information (such as iid, sex and phenotype) are
        stored in the dataframe datadf, index is the Individual ID, 
        with following columns for metainfo:

            * family_id   -> Family ID
            * paternal_id -> Paternal ID
            * maternal_id -> Maternal ID
            * sex         -> Sex (1=male; 2=female; other=unknown)
            * phenotype   -> Phenotype (-9, or 0 for unknown)
            * population  -> Population string (e.g. 'ASW' - 'YRI')
            * rest are SNP rs (ids)

        More information is given in infodf:

            * Chromosome:
                - autosomal chromosemes                -> 1-22
                - X    X chromosome                    -> 23
                - Y    Y chromosome                    -> 24
                - XY   Pseudo-autosomal region of X    -> 25
                - MT   Mitochondrial                   -> 26
            * Relative Positon (to Chromosome) [base pairs]

        """,
                                 'citation': """Gibbs, Richard A., et al. "The international HapMap project." Nature 426.6968 (2003): 789-796.""",
                                 'license' : """International HapMap Project Public Access License (http://hapmap.ncbi.nlm.nih.gov/cgi-perl/registration#licence)""",
                                 'size' : 2*1729092237 + 62265},

                  'singlecell' : {'urls' : ["http://staffwww.dcs.sheffield.ac.uk/people/M.Zwiessele/data/singlecell/"],
                                  'files' : [['singlecell.csv']],
                                  'details' : "qPCR Singlecell experiment in Mouse, measuring 48 gene expressions in 1-64 cell states. The labels have been created as in Guo et al. [2010]",
                                  'citation' : "Guoji Guo, Mikael Huss, Guo Qing Tong, Chaoyang Wang, Li Li Sun, Neil D. Clarke, Paul Robson, Resolution of Cell Fate Decisions Revealed by Single-Cell Gene Expression Analysis from Zygote to Blastocyst, Developmental Cell, Volume 18, Issue 4, 20 April 2010, Pages 675-685, ISSN 1534-5807, http://dx.doi.org/10.1016/j.devcel.2010.02.012. (http://www.sciencedirect.com/science/article/pii/S1534580710001103) Keywords: DEVBIO",
                                  'license' : "ScienceDirect: http://www.elsevier.com/locate/termsandconditions?utm_source=sciencedirect&utm_medium=link&utm_campaign=terms",
                                  'size' : 233.1,
                                  }
                  }

with open('data_resources.json', 'w') as f:
    print "writing data_resources"
    json.dump(data_resources, f)
