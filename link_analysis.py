links = ['https://assetstore.unity.com/packages/2d/characters/hero-nad-opponents-animation-140776',
'https://assetstore.unity.com/packages/2d/characters/cute-2d-girl-wizard-155796',
'https://assetstore.unity.com/packages/2d/characters/monsters-creatures-fantasy-167949',
'https://assetstore.unity.com/packages/2d/characters/prototype-hero-demo-pixel-art-186233',
'https://assetstore.unity.com/packages/2d/characters/warrior-free-asset-195707',
'https://assetstore.unity.com/packages/2d/characters/bandits-pixel-art-104130',
'https://assetstore.unity.com/packages/2d/characters/hero-knight-pixel-art-165188',
'https://assetstore.unity.com/packages/audio/sound-fx/minimal-ui-sounds-78266',
'https://assetstore.unity.com/packages/audio/sound-fx/shooting-sound-177096',
'https://assetstore.unity.com/packages/audio/sound-fx/free-sound-effects-pack-155776',
'https://assetstore.unity.com/packages/audio/sound-fx/foley/footsteps-essentials-189879',
'https://assetstore.unity.com/packages/audio/sound-fx/transportation/vehicle-essentials-194951',
'https://assetstore.unity.com/packages/audio/sound-fx/free-casual-game-sfx-pack-54116',
'https://assetstore.unity.com/packages/audio/music/absolutely-free-music-4883',
'https://assetstore.unity.com/packages/audio/music/8bit-music-album-051321-196147',
'https://assetstore.unity.com/packages/audio/music/casual-game-bgm-5-135943',
'https://assetstore.unity.com/packages/audio/ambient/sci-fi/universe-sounds-free-pack-118865',
'https://assetstore.unity.com/packages/audio/ambient/horror-ambient-album-060319-147877',
'https://assetstore.unity.com/packages/audio/ambient/nature/nature-essentials-208227',
'https://assetstore.unity.com/packages/tools/ai/spawner-free-2704',
'https://assetstore.unity.com/packages/tools/ai/procedural-level-generator-136626',
'https://assetstore.unity.com/packages/tools/ai/candice-ai-for-games-148441',
'https://assetstore.unity.com/packages/tools/ai/vide-dialogues-69932',
'https://assetstore.unity.com/packages/vfx/particles/cartoon-fx-free-109565',
'https://assetstore.unity.com/packages/vfx/particles/fire-explosions/procedural-fire-141496']

def get_link_info(link):
    # Removes the part of link that is uniform throughout
    trimmed_link = link[38:]
    # Puts all of the categories at beginning of info array
    info = trimmed_link.split('/')
    title_id = info[len(info) - 1]
    info.remove(title_id)
    title_id = title_id.split('-')
    id = title_id[len(title_id) - 1]
    # ID added to info[len(info) - 2]
    info.append(id)
    title_id.remove(id)
    title = " ".join(title_id)
    # Title added to info[len(info) - 1]
    info.append(title)
    return info

# prints each link with its corresponding info array
for link in links:
    print(link)
    info = get_link_info(link)
    categories = info[:len(info) - 2]
    print("Title: "+info[len(info) - 1]+ ", Asset ID: "+info[len(info) -2]+ ", Categories: "+ ', '.join(map(str, categories)))

