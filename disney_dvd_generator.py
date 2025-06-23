import moviepy.editor as mpy

def create_slide(text, duration=3, fontsize=70, color='white', bg_color='black'):
    return mpy.TextClip(text, fontsize=fontsize, color=color, bg_color=bg_color, size=(1280, 720)).set_duration(duration)

def generate_opening():
    return create_slide("FBI Warning\n\nUnauthorized copying is punishable under federal law.", duration=4, fontsize=50)

def generate_disney_logo():
    return create_slide("Disney DVD\n\nWalt Disney Home Entertainment", duration=3, fontsize=60, color='gold')

def generate_preview(title):
    return create_slide(f"Coming Soon to Own on DVD & Video\n\n{title}", duration=3, fontsize=40, color='yellow')

def generate_sneak_peek(title):
    return create_slide(f"Sneak Peek\n\n{title}", duration=3, fontsize=45, color='cyan')

def generate_menu(options):
    slides = [create_slide("Disney DVD Main Menu", duration=3, fontsize=60, color='orange')]
    for option in options:
        slides.append(create_slide(f"Menu Option: {option}", duration=2, fontsize=45, color='orange'))
    return mpy.concatenate_videoclips(slides)

def generate_closing():
    return create_slide("Now Available to Own on DVD & Video", duration=3, fontsize=40, color='yellow')

def main():
    # Compose your sequence here
    opening = generate_opening()
    logo = generate_disney_logo()
    preview = generate_preview("The Lion King II: Simba's Pride")
    sneak = generate_sneak_peek("Tarzan II")
    menu = generate_menu(["Play Movie", "Scene Selection", "Bonus Features", "Set Up"])
    closing = generate_closing()

    final_video = mpy.concatenate_videoclips([opening, logo, preview, sneak, menu, closing])
    final_video.write_videofile("disney_dvd_experience.mp4", fps=24)

if __name__ == "__main__":
    main()