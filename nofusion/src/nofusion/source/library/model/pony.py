# For Setting up Cyber Realistic
from ....source import civitai_fetch_checkpoints, civitai_fetch_loras


def source_model_pony_cyber_realistic():
    civitai_fetch_checkpoints("CyberRealisticPony", "2071650")

    # civitai_checkpoint_fetch("StableIllustrious","2091367")
    # For Illustrious
    civitai_fetch_loras("AgeSlider", "448977")
    civitai_fetch_loras("CInMouth", "1909950")
    civitai_fetch_loras("RealisticC", "1629360")
