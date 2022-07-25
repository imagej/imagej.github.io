---
mediawiki: Colocalization_Threshold
name: "Colocalization Threshold"
title: Colocalization Threshold
categories: [Colocalization,Color Processing]
release-date: "june 2009"
website: /imaging/colocalization-analysis#colocalization-threshold
dev-status: "no longer actively supported, unlikely to be stable enough for real use. Use [Coloc\_2](/plugins/coloc-2)"
team-maintainer: "@chalkie666"
team-founder: 'Tony Collins (and others?)'
---

{% include warning/deprecated
  old="the Colocalization Threshold plugin"
  new="[Coloc 2](/plugins/coloc-2)" %}


{% capture source%}
{% include github org='fiji' repo='Colocalisation_Analysis' branch='master' source='Colocalisation_Threshold.java' %}, modified from [MBF ImageJ](/software/mbf-imagej)
{% endcapture %}
{% include info-box filename='Colocalization.jar' source=source  %}

## Purpose

Sets the thresholds for colocalization analysis, and also calculates Manders coefficients, 2D histogram / scatter plot, and other stats.

## Documentation

See the great documentation for this plugin at [Colocalization Analysis\#Colocalization\_Threshold](/imaging/colocalization-analysis#colocalization-threshold). The method is that implemented in Costes et al. This uses a Pearson's correlation above and below the thresholds to iteratively find where the correlation between the two images is 0 and sets the thresholds there. It is pretty robust and importantly is reproducible and non subjective.

Use of this plugin should be followed by use of the [Colocalization Test](/plugins/colocalization-test) plugin, to see of the results are statistically significant and better then random overlap of the signal in the images.

See also the [Colocalization Analysis](/imaging/colocalization-analysis) tutorial.

  
