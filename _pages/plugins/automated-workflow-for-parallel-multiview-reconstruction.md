---
title: Automated workflow for parallel Multiview Reconstruction
name: Automated workflow for parallel Multiview Reconstruction
categories: [Transform,Registration,Deconvolution]
source-url: https://github.com/mpicbg-scicomp/snakemake-workflows
source-label: on GitHub
team-developers: 
 - Christopher Schmied | /people/schmiedc
 - Peter Steinbach | /people/psteinb
 - Pavel Tomancak | /people/tomancak
team-maintainers: 
 - Christopher Schmied | /people/schmiedc
release-date: 'July 2015'
---

{% include notice icon="info" content='Latest release: March 2016' %}

# Citation

Please note that the automated workflow for processing SPIM data on a cluster is based on a publication. If you use it successfully for your research please be so kind to cite the following work:

-   C. Schmied, P. Steinbach, T. Pietzsch, S. Preibisch, P. Tomancak (2015) "An automated workflow for parallel processing of large multiview SPIM recordings." *Bioinformatics*, Dec 1; doi: 10.1093/bioinformatics/btv706 [Webpage](http://bioinformatics.oxfordjournals.org/content/early/2015/12/30/bioinformatics.btv706.long)

The automated workflow is based on the Fiji plugins **[Multiview Reconstruction](/plugins/multiview-reconstruction)** and **[BigDataViewer](/plugins/bdv)**. Please refer to and cite the following publications:

-   S. Preibisch, S. Saalfeld, J. Schindelin and P. Tomancak (2010) "Software for bead-based registration of selective plane illumination microscopy data", *Nature Methods*, **7**(6):418-419.[Webpage](http://www.nature.com/nmeth/journal/v7/n6/full/nmeth0610-418.html)
-   S. Preibisch, F. Amat, E. Stamataki, M. Sarov, R.H. Singer, E. Myers and P. Tomancak (2014) "Efficient Bayesian-based Multiview Deconvolution", *Nature Methods*, **11**(6):645-648. [Webpage](http://www.nature.com/nmeth/journal/v11/n6/full/nmeth.2929.html)
-   T. Pietzsch, S. Saalfeld, S. Preibisch, P. Tomancak (2015) "BigDataViewer: visualization and processing for large image data sets." *Nature Methods*, **12**(6)481–483. [Webpage](http://www.nature.com/nmeth/journal/v12/n6/full/nmeth.3392.html)

# Multiview reconstruction

In the **[Multiview Reconstruction](/plugins/multiview-reconstruction)** (MVR) pipeline all results are written into an XML. This poses new problems for cluster processing, because several concurrently running jobs need to update the same file.

Stephan Preibisch solved that problem by allowing to write one XML file per job (usually a timepoint) and then merging the job specific XMLs into one XML for the entire dataset.

In practice it means the following steps need to be executed:

-   Define XML dataset - creates one XML for the entire timelapse
-   Re-save data as HDF5 - converts data into HDF5 container optimised for fast access in **[BigDataViewer](/plugins/bdv)**
-   Run per time-point registrations - creates as many XMLs as there are timepoints
-   Merge XMLs - consolidates the per-timepoint XMLs back into a single XML

Some new parameters are introduced and some old parameters change names. Therefore, use the ***[config.yaml](#config.yaml)*** described in this chapter to process with the MVR pipeline.

Outdated versions of the cluster processing scripts on which this workflow is based on you can find [here](/plugins/spim-registration/on-cluster)

# Logic of workflow

We map and dispatch the workflow logic either on a single machine or on a HPC cluster using the automated workflow engine **Snakemake**. Within the *Snakefile* the workflow with the processing steps and the input and output rules is defined. Each of these steps call a Fiji *beanshell* script. These scripts in turn drive the processing via Fiji.

The current workflow consists of the following steps. It covers the prinicipal processing for timelapse multiview SPIM processing:

1. define czi or tif dataset.

2. resave into hdf5.

3. detect and register interest points.

4. merge xml, creates XML for registered dataset.

5. timelapse registration.

6. optional for dual channel dataset: duplicate transformations

7. optional for deconvolution: external transformation

8. average-weight fusion/deconvolution

9. define output

10. resave output into hdf5, creates XML for fused dataset.

# Supported datasets

The scripts are supporting multiple angles, multiple channels and multiple illumination direction without adjusting the Snakefile or .bsh scripts.

Using spimdata version: 0.9-revision

Using SPIM registration version 2.3.9

Supported datasets are in the following format:

Using Zeiss Lightsheet Z.1 Dataset (LOCI)

	Multiple timepoints:  YES (one file per timepoint) or (all time-points in one file)
	Multiple channels:  YES (one file per channel) or (all channels in one file)
	Multiple illumination directions: YES (one file per illumination direction)
	Multiple angles: YES (one file per angle)

Using LOCI Bioformats opener (.tif)

	Multiple timepoints: YES (one file per timepoint) or (all time-points in one file)
	Multiple channels: YES (one file per channel) or (all channels in one file)
	Multiple illumination directions: YES (one file per illumination direction) => not tested yet
	Multiple angles: YES (one file per angle)

Using ImageJ Opener (.tif):

	Multiple timepoints: YES (one file per timepoint)
	Multiple channels: YES (one file per channel)
	Multiple illumination directions: YES (one file per illumination direction) => not tested yet
	Multiple angles: YES (one file per angle)

# Fiji for workflow

You can download a Fiji version that we have tested for compatibility with the automated cluster processing here:

**https://doi.org/10.5281/zenodo.6338071**

It is important to note that we can only guarantee the proper execution of the workflow with the provided Fiji version. We will from time to time upgrade to cover the latest changes in the plugins.

# Snakemake for workflow

**[Snakemake](https://snakemake.readthedocs.io/en/stable/)** (command-line workflow engine) is used to automatically execute individual steps in the workflow. The workflow documented on this page was tested with snakemake 3.3 (interfaced with **[PyYAML](http://www.pyyaml.org)**(version 3.11) and **[python drmaa](https://github.com/pygridtools/drmaa-python)** (version 0.7.6) support.

# Automated Multiview Reconstruction workflow

Clone the repository for the workflow from **[github](https://github.com/mpicbg-scicomp/snakemake-workflows)**.

{% highlight shell %}
git clone https://github.com/mpicbg-scicomp/snakemake-workflows.git
{% endhighlight %}

The repository contains the example configuration scripts for single and dual channel datasets, the Snakefile which defines the workflow, the beanshell scripts which drive the processing via Fiji and a cluster.json file which contains information for the cluster queuing system.

## timelapse directory

{% highlight shell %}
/path/to/repository/spim_registration/timelapse/
├── README.md
├── Snakefile
├── cluster.json
├── config.yaml
├── deconvolution.bsh
├── define_czi.bsh
├── define_output.bsh
├── define_tif_zip.bsh
├── duplicate_transformations.bsh
├── export.bsh
├── export_output.bsh
├── fusion.bsh
├── registration.bsh 
├── timelapse_registration.bsh
├── timelapse_utils.py
├── transform.bsh       
└── xml_merge.bsh           
{% endhighlight %}

-   The *Snakefile* contains the name of the processing step as well as the input and output rules for the processing.
-   *config.yaml* contains the parameters that configure the beanshell scripts found in the data directory.
-   *cluster.json* contains the resource information (processing time, number of cores and memory) for the queuing system.
-   *\*.bsh* scripts contain the instructions for Fiji to run the processing.

## tools directory

The tool directory contains scripts for common file format pre-processing. Some datasets are currently only usable when resaving them into *.tif*:

-   discontinous *.czi* datasets
-   *.czi* dataset with multiple groups
-   *.ome.tiff* files

The *master\_preprocessing.sh* file is the configuration script that contains the information about the dataset that needs to be resaved. In the *czi\_resave* as well as the *ometiff\_resave* directory you will find the the *create-resaving-jobs.sh* script that creates a job for each time point. The *submit-jobs* script sends these jobs to the cluster where they call the *resaving.bsh* or *ometiff\_resave.bsh* script. The beanshell then uses the Fiji macro and resaves the files. The resaving of *.czi* files is using LOCI bioformats and preserves the metadata.

{% highlight shell %}
/path/to/repository/spim_registration/tools/
├── czi_resave/
	├── create-resaving-jobs.sh
	├── resaving.bsh
	└── submit-jobs
├── ometiff_resave/
	├── create-ometiff_resave.sh
	├── ometiff_resave.bsh
	└── submit-jobs
└──  master_preprocessing.sh
{% endhighlight %}

## cluster\_tools directory

The cluster tools directory contains the libraries for GPU deconvolution and the virtual frame buffer (xvfb) for running Fiji headless.

```shell
libFourierConvolutionCUDALib.so
xvfb-run
```

## sysconfcpus

We use **[Libsysconfcpus](http://www.kev.pulo.com.au/libsysconfcpus/)** to restrict how many cores Fiji is using on the cluster.

Compile with:

{% highlight makefile %}
CFLAGS=-ansi ./configure --prefix=$PREFIX
make
make install
{% endhighlight %}

where PREFIX is the installation directory. ANSI mode is necessary when compiling with our default GCC version, 4.9.2. It may or may not be necessary with older versions.

# Command line

It is very likely that the cluster computer does not run ANY Graphical User Interface and relies exclusively on the command line. Steering a cluster from the command line is fairly easy - I use about 10 different commands to do everything I need to do. Since the Linux command line may be unfamiliar to most biologists we start a separate **[Linux command line tutorial](/tutorials/linux-command-line)** and **[Software Carpentry's workshop The Unix Shell](http://swcarpentry.github.io/shell-novice/)** page that explains the bare essentials.

# Initial setup of the workflow

After you cloned the snakemake-workflows repository you need to configure the *config.yaml* for your setup. This means you need to specify the directory for your Fiji, the location of the xvfb-run and the location for the GPU deconvolution libraries. Go into the timelapse directory of the snakemake-workflows and open the *config.yaml* with your preferred editor for example nano and change the settings in section *7. Software directories*:

{% highlight shell %}
cd snakemake-workflows/spim_registration/timelapse/
nano config.yaml
{% endhighlight %}

{% highlight shell %}
# ============================================================================
# 7. Software directories
# 
# Description: paths to software dependencies of processing
# Options: Fiji location
#          beanshell and snakefile diretory
#          directory for cuda libraries
#          xvfb setting
#          sysconfcpus setting
# ============================================================================
# current working Fiji
fiji-app: "/sw/users/schmied/packages/2015-06-30_Fiji.app.cuda/ImageJ-linux64",
# bean shell scripts and Snakefile
bsh_directory: "/projects/pilot_spim/Christopher/snakemake-workflows/spim_registration/timelapse/",
# Directory that contains the cuda libraries
directory_cuda: "/sw/users/schmied/cuda/",
# xvfb 
fiji-prefix: "/sw/users/schmied/packages/xvfb-run -a",       # calls xvfb for Fiji headless mode
sysconfcpus: "sysconfcpus -n",
memory-prefix: "-Xmx"
{% endhighlight %}

After this initial setup you can proceed to modify the *config.yaml* for your specific dataset.

# Setup for the dataset

You can download a 5 view, single channel .czi example dataset here:

**http://tomancak-srv1.mpi-cbg.de/~schmied/**

The example dataset looks like this:

{% highlight shell %}
/path/to/data/
├── exampleSingleChannel.czi
├── exampleSingleChannel(1).czi
├── exampleSingleChannel(2).czi
├── exampleSingleChannel(3).czi
└── exampleSingleChannel(4).czi
{% endhighlight %}

For processing, the dataset directory will also contain the config.yaml file for the specific dataset. Go to your dataset directory and make a symlink for the config.yaml:

{% highlight shell %}
cd /path/to/data/
ln -s /path/snakemake-workflows/spim_registration/timelapse/config.yaml
{% endhighlight %}

Now the dataset directory has a symlink for the config.yaml:

{% highlight shell %}
/path/to/data/
├── exampleSingleChannel.czi
├── exampleSingleChannel(1).czi
├── exampleSingleChannel(2).czi
├── exampleSingleChannel(3).czi
├── exampleSingleChannel(4).czi
└── config.yaml         # copied/symlinked from this repo
{% endhighlight %}

## *config.yaml*

The entire processing is controlled via the yaml file.

The key parameters for the processing are found in the first (common) part of the yaml file. These parameters are usually dataset and user dependent. The second part contains the advanced and manual overrides for each processing step. These steps correspond to the rules in the snakefile.

## Setting up the *config.yaml* file for processing

### Processing switches

In the first section you need to decide which processing you want to carry out. Open the *config.yaml* file:

{% highlight shell %}
cd snakemake-workflows/spim_registration/timelapse/
nano config.yaml
{% endhighlight %}

The *transformation\_switch* switches between normal single channel/ multi channel processing where all channels contain beads for registration and multi channel processing where only one channel contains beads. If there are channels present without beads the transformations of the other channels need to be copied in order to register them.

Set the *transformation\_switch* to *timelapse* to do single channel processing or multichannel processing where all channels contain beads:

{% highlight yaml %}
transformation_switch: "timelapse",
{% endhighlight %}

Set the *transformation\_switch* to *timelapse\_duplicate* to duplicate the transformation from one channel to others:

{% highlight yaml %}
transformation_switch: "timelapse_duplicate",
{% endhighlight %}

The *fusion\_switch* decides between weighted-average fusion and deconvolution. Set the *fusion\_switch* to *fusion* to do weighted-average fusion:

{% highlight yaml %}
fusion_switch: "fusion",
{% endhighlight %}

Set the *fusion\_switch* to *deconvolution* to perform deconvolution:

{% highlight yaml %}
fusion_switch: "deconvolution",
{% endhighlight %}

### General Settings

In the the next section specify the name of the dataset. This will be the name of the *HDF5* file and the *XML* file:

{% highlight yaml %}
hdf5_xml_filename: '"dataset_one"',
{% endhighlight %}

Then specify the number of time points of the dataset. The example dataset has 2 time points. The processing of each time point runs in parallel on the cluster.

{% highlight yaml %}
ntimepoints: 2,  
{% endhighlight %}

Then specify the angles, the channels and the illumination side. If you resaved data into *.tif* from *.czi* then give the appropriate numbers (i.e. 0,1). The values are separated by a comma:

{% highlight yaml %}
angles: "0,72,144,216,288",
channels: "green", 
illumination: "0", 
{% endhighlight %}

If you want to process dual channel datasets use two different names for the channels:

{% highlight yaml %}
angles: "0,72,144,216,288",
channels: "green,red", 
illumination: "0", 
{% endhighlight %}

#### Settings for .czi files

If you process *.czi* files then give the name of the first *.czi* (file without index):

{% highlight yaml %}
first_czi: "exampleSingleChannel.czi",
{% endhighlight %}

#### Settings for .tif datasets

For processing of *.tif* files give the pattern of the files and if you process single channel datasets or dual channel datasets:

{% highlight yaml %}
image_file_pattern: 'img_TL{{t}}_Angle{{a}}.tif',
multiple_channels: '"NO (one channel)"', 
{% endhighlight %}

For datasets with multiple channels the files can be separated by channel or each file can contain both channels. For multi channel datasets with separated files per channel give additionally the channel information of the *image\_file\_pattern*

{% highlight yaml %}
image_file_pattern: 'img_TL{{t}}_Angle{{a}}_Channels{{c}}.tif',
multiple_channels: '"YES (one file per channel)"', 
{% endhighlight %}

If the files contain both channels then leave out the channel information in the *image\_file\_pattern*. And specify for *multiple\_channels* that you want to process multi channel datasets:

{% highlight yaml %}
image_file_pattern: 'img_TL{{t}}_Angle{{a}}.tif',
multiple_channels: '"YES (all channels in one file)"', 
{% endhighlight %}

### Detection and registration

To carry out the registration specify the channels for the data containing beads. For single channel data and multi channel data where all channels contain beads for registration you want to select the following: As interest points specify '"beads"'. For multi channel datasets indicate '"beads,beads"':

{% highlight yaml %}
reg_process_channel: '"All channels"',
reg_interest_points_channel: '"beads"',
{% endhighlight %}

If you have dual channel datasets where only one channel contains beads specify that you want to select only one channel. Also specify the source and target channels. And specify the correct channel that should not be registered:

{% highlight yaml %}
reg_process_channel: '"All channels"',
source_channel: "red",
target_channel: "green",
reg_interest_points_channel: '"[DO NOT register this channel],beads"',
{% endhighlight %}

Next give the parameters for the detection method. Select the method which is used for registration (i.e. Difference-of-Mean or Difference-of-Gaussian). We recommend using Difference-of-Gaussian. Give the information for radius 1 and 2 as well as the threshold that you retrieved by processing the reference time point with the Graphical user interface:

{% highlight yaml %}
type_of_detection: '"Difference-of-Gaussian"',
sigma: '1.3',
reg_threshold: '0.005',
{% endhighlight %}

For Difference-of-Mean registration specify radius\_1, radius\_2 and the threshold:

{% highlight yaml %}
type_of_detection: '"Difference-of-Gaussian"',
reg_radius_1: '2',
reg_radius_2: '3',
reg_threshold: '0.005',
{% endhighlight %}

### Timelapse registration

Specify which time point should be used as reference time point. We generally use a time point in the middle of the dataset:

{% highlight yaml %}
reference_timepoint: '1', 
{% endhighlight %}

### Weighted-average fusion

For the weighted-average fusion specify the downsampling factor and the bounding box determined in the GUI processing on the reference time point. The bounding box is for the Weighted-average fusion independent of the downsampling:

{% highlight yaml %}
downsample: '1', 
minimal_x: '274',
minimal_y: '17',
minimal_z: '-423',
maximal_x: '1055',
maximal_y: '1928',
maximal_z: '480',
{% endhighlight %}

### Multiview deconvolution

#### External transformation

If you want to use downsampling for the multiview deconvolution set the *external\_trafo\_switch* to *external\_trafo*. Without downsampling use *\_transform*. The matrix for the external transformation specifies the downsampling. Here it is set to 2x downsampling:

{% highlight yaml %}
external_trafo_switch: "external_trafo",
matrix_transform: '"0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0"',
{% endhighlight %}

#### Deconvolution settings

To carry out the deconvolution specify the numbers of iterations as well as the bounding box. For the multiview deconvolution the bounding box needs to take the downsampling into account:

{% highlight yaml %}
iterations: '15',
minimal_x_deco: '137',
minimal_y_deco: '-8',
minimal_z_deco: '-211',
maximal_x_deco: '527',
maximal_y_deco: '964',
maximal_z_deco: '240',
{% endhighlight %}

Then specify the source for the point-spread-function (PSF). For single channel datasets it is just '"beads"'.

{% highlight yaml %}
detections_to_extract_psf_for_channel: '"beads"',
{% endhighlight %}

For dual channel datasets its '"beads,beads"'

{% highlight yaml %}
detections_to_extract_psf_for_channel: '"beads,beads"',
{% endhighlight %}

If you process multi channel datasets where only one channel contains beads then specify which channel does not contain beads:

{% highlight yaml %}
detections_to_extract_psf_for_channel: '"[Same PSF as channel red],beads"',
{% endhighlight %}

### Software directories

Here the directories for the Fiji, *beanshell* scripts, CUDA libraries and xvfb are stored. Also the prefix for sysconfcpus and the memory prefix for Fiji are stored:

{% highlight yaml %}
# current working Fiji
fiji-app: "/sw/users/schmied/packages/2015-06-30_Fiji.app.cuda/ImageJ-linux64",
# bean shell scripts and Snakefile
bsh_directory: "/projects/pilot_spim/Christopher/snakemake-workflows/spim_registration/timelapse/",
# Directory that contains the cuda libraries
directory_cuda: "/sw/users/schmied/cuda/",
# xvfb 
fiji-prefix: "/sw/users/schmied/packages/xvfb-run -a",       # calls xvfb for Fiji headless mode
sysconfcpus: "sysconfcpus -n",
memory-prefix: "-Xmx"
{% endhighlight %}

### Fiji Resource settings

Here the resource restrictions for Fiji with the number of cores and memory are specified for each processing step. These settings need to match the cluster.json file:

{% highlight json %}
Fiji_resources: {
  # setting for hdf5 resave:
  num_cores_hdf5: 3,
  mem_hdf5: "20g",
  # setting for registration:
  num_cores_reg: 4,
  mem_reg: "40g",
  # setting for timelapse registration:
  num_cores_time: 3,
  mem_time: "50g",
  # settings for average fusion:
  num_cores_fusion: 6,
  mem_fusion: "50g",
  # settings for deconvolution:
  num_cores_deco: 12,
  mem_deco: "110g",
  # settings for resaving of output:
  num_cores_output: 3,
  mem_output: "20g"
{% endhighlight %}

### Advanced settings

In the advanced settings are more options for further refining the processing. These settings should only be changed when necessary.

## *cluster.json*

The *cluster.json* contains the resource information for the queuing system. It should match the Fiji resource settings.

{% highlight json %}
    {
        "__default__" :
        {
        "lsf_extra" : "-R \"span[hosts=1]\"",
        "lsf_q" : "short"   
        },
        
        "hdf5_xml" :
        {
        "lsf_extra" : "-n 3 -R \"span[hosts=1] rusage[mem=20000]\""
        },

        "resave_hdf5" : 
        {
        "lsf_extra" : "-n 3 -R \"span[hosts=1] rusage[mem=20000]\""
        },

        "registration" :
        {
            "lsf_extra" : "-n 4 -R \"span[hosts=1] rusage[mem=40000]\""
        },
        
        "timelapse" : 
        {
            "lsf_extra" : "-n 6 -R \"span[hosts=1] rusage[mem=50000]\""
        },

        "external_transfrom" :
        {
            "lsf_extra" : "-R \"span[hosts=1] rusage[mem=10000]\""
        },

        "fusion" : 
        {
            "lsf_extra" : "-n 6 -R \"span[hosts=1] rusage[mem=50000]\"",
            "lsf_q" : "short"
        },

        "deconvolution" :
        {
            "lsf_extra" : "-n 12 -R \"span[hosts=1] rusage[mem=110000]\"",
        "lsf_q" : "gpu"
        },
        
        "resave_hdf5_output" :
        {
        "lsf_extra" : "-n 3 -R \"span[hosts=1] rusage[mem=20000]\""
        }
    }
{% endhighlight %}

## Submitting Jobs

We recommend to execute Snakemake within **[screen](https://www.gnu.org/software/screen/manual/screen.html)**. To execute Snakemake you need to call Snakemake, specify the number of jobs, the location of the data and to dispatch jobs to a cluster with the information for the queuing system. Here is a list of commands and flags that are used for the Snakemake workflow:

Local back end: /path/to/snakemake/snakemake -j 1 -d /path/to/data/

Flag for number of jobs run in parallel: -j <number of jobs>

Flag for specifying data location: -d /path/to/data/

Flag for dry run of snakemake: -n

Force the execution of a rule: -R <name of rule>

For DRMAA back end add: --drmaa " -q {cluster.lsf\_q} {cluster.lsf\_extra}"

For Lsf backend add: --cluster "bsub -q {cluster.lsf\_q} {cluster.lsf\_extra}"

To specify the configuration script for the queuing system: --cluster-config ./cluster.json

To save error and output files of cluster add: --drmaa " -q {cluster.lsf\_q} {cluster.lsf\_extra} -o test.out -e test.err" --cluster "bsub -q {cluster.lsf\_q} {cluster.lsf\_extra} -o test.out -e test.err"

The commands to execute snakemake would then look like this:

If DRMAA is supported on your cluster:

{% highlight shell %}
/path/to/snakemake/snakemake -j 2 -d /path/to/data/ --cluster-config ./cluster.json --drmaa " -q {cluster.lsf_q} {cluster.lsf_extra}"
{% endhighlight %}

If not:

{% highlight shell %}
/path/to/snakemake/snakemake -j 2 -d /path/to/data/ --cluster-config ./cluster.json --cluster "bsub -q {cluster.lsf_q} {cluster.lsf_extra}"
{% endhighlight %}

For error and output of the cluster add -o test.out -e test.err e.g.:

DRMAA

{% highlight shell %}
/path/to/snakemake/snakemake -j 2 -d /path/to/data/ --cluster-config ./cluster.json --drmaa " -q {cluster.lsf_q} {cluster.lsf_extra} -o test.out -e test.err"
{% endhighlight %}

LSF

{% highlight shell %}
/path/to/snakemake/snakemake -j 2 -d /path/to/data/ --cluster-config ./cluster.json --cluster "bsub -q {cluster.lsf_q} {cluster.lsf_extra} -o test.out -e test.err"
{% endhighlight %}

Note: the error and output of the cluster of all jobs are written into these files.

## Log files and supervision of the pipeline

The log files are written into a new directory in the data directory called "logs". The log files are ordered according to their position in the workflow. Multiple or alternative steps in the pipeline are indicated by numbers.

force certain rules: use the -R flag to rerun a particular rule and everything downstream -R <name of rule>

# Cluster

Every cluster is different both in terms of the used hardware and the software running on it, particularly the scheduling system. Here we use a cluster computer at the MPI-CBG that consists of **44** nodes each with **12** Intel Xeon E5-2640 cores running @ 2.50 GHz and enjoying **128GB** of memory. The cluster nodes have access to 200TB of data storage provided by a dedicated Lustre distributed file system, suffice to say that it is optimised for high performance input/output (read/write) operations which is crucial for the SPIM data volumes.

Each node of this cluster runs CentOS 6.3 Linux distribution. The queuing system running on the MPI-CBG cluster is LSF. The basic principles of job submission are the same across queuing systems, but the exact syntax will of course differ.

  
