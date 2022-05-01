---
title: OpenMPI Plugin Extensions
categories: [Scripting]
name: Parallel Ops
team-developers: Daniel Trnka, Michal Krumnickl
team-maintainers: Daniel Trnka
source-url: https://github.com/fiji-hpc/scijava-parallel-mpi
source-label: on GitHub
---

{% include notice icon="warning" content='Please Note: This version of the documentation is outdated. We recommend reading the [guide](https://github.com/fiji-hpc/scijava-parallel-mpi/wiki/How-to-Install-and-Run) instead. It contains current information on new features.' %}

## General information

### Motivation

OpenMPI, despite being relatively old, still remains the most dominant programming model used in high-performance computing (HPC). As of today Fiji supports the GPU parallelization through [CLIJ](/plugins/clij) and allows executing automated HPC workflows by means of [Automated\_workflow\_for\_parallel\_Multiview\_Reconstruction](/plugins/automated-workflow-for-parallel-multiview-reconstruction). However, there are still no genuine internally parallel plugins developed specifically for deployment on large scale parallel machines like HPC clusters or supercomputers. This is a preliminary OpenMPI framework for Fiji and model parallel implementations of the most common image processing operations included in ImageJ.

### Extensions Description

This presents a set of Ops adapted to herein presented OpenMPI wrapper, jointly comprising a solution designed to be seamlessly used in any existing ImageJ2 code. Moreover, framework automatically initializes and disposes connections to the OpenMPI environment, making available OpenMPI implementations for the most frequent operations covered by Ops. The package contains example implementations for fundamental image processing functions as well as basic math, logical and statistics operations.

## Installation

TBD

## How to use

In order to demonstrate convenience of this approach, we prepared an example of parallelized convolution. We used Python for readers' convenience, however plugins can be invoked from any other scripting language supported by Fiji.

```python
kernel = ops.run("create.img", [3, 3], FloatType())
for p in kernel:
 p.set(1.0/kernel.size())

def fn():
 output = ops.create().img(input)
 ops.filter().convolve(output, Views.extendMirrorSingle(input), kernel)
 return output

input = scifio.datasetIO().open(input_path)
output = Measure.benchmark(fn, rounds)
scifio.datasetIO().save(output, output_path)
 ```

The Listing shows the OpenMPI implementation with initialization of a 3×3 blur kernel (lines 1-3), definition of a processing function with convolution (it reuses already existing implementation of a convolution filter in ImageJ2) on lines 5-8 and finally its execution in the benchmark mode to measure execution times (the variable rounds defines the number of repetitions).

Noticeably, using the OpenMPI extension does not add any extra layer as long as data are available in a form of IterableInterval.

### Debugging

Debugging printouts on the console shows the node allocation and dataset division. The following listing shows the dataset divided to 6 nodes.

    Fri Jun 19 08:36:49 2020[1,2]<stdout>:Chunk{data=test.tif, offset=13334, len=6667, chunks=1}
    Fri Jun 19 08:36:49 2020[1,0]<stdout>:Chunk{data=test.tif, offset=0, len=6667, chunks=1}
    Fri Jun 19 08:36:49 2020[1,5]<stdout>:Chunk{data=test.tif, offset=33335, len=6665, chunks=1}
    Fri Jun 19 08:36:49 2020[1,1]<stdout>:Chunk{data=test.tif, offset=6667, len=6667, chunks=1}
    Fri Jun 19 08:36:49 2020[1,4]<stdout>:Chunk{data=test.tif, offset=26668, len=6667, chunks=1}
    Fri Jun 19 08:36:49 2020[1,3]<stdout>:Chunk{data=test.tif, offset=20001, len=6667, chunks=1}
