from .component import Component

### 🔧 **Core & Utility Components**
from .world.transform import Transform
from .utilities.tag import Tag

# from .utilities.name import Name
from .utilities.active import Active

### 🎨 **Rendering Components**
from .render.renderer_frame import RendererFrame
from .render.sprite_renderer import SpriteRenderer

# from .render.animator import Animator
# from .render.tilemap_renderer import TilemapRenderer
# from .render.text_renderer import TextRenderer
# from .render.z_index import ZIndex

### 🧠 **Logic & Control Components**
# from .script import Script
# from .finite_state_machine import FiniteStateMachine
# from .event_listener import EventListener
# from .timer import Timer

### 🕹️ **Input Components**
# from .input.input_listener import InputListener
# from .input.clickable import Clickable
# from .input.draggable import Draggable

### 🧱 **Physics & Collision**
# from .rigid_body import RigidBody
# from .collider import Collider
# from .collision_handler import CollisionHandler
# from .trigger_zone import TriggerZone

### 🔊 **Audio Components**
# from .audio_source import AudioSource
# from .audio_listener import AudioListener
# from .music_player import MusicPlayer

### 🎮 **Game Systems**
# from .inventory import Inventory
# from .health import Health
# from .experience import Experience
# from .interactable import Interactable
# from .spawner import Spawner

### 🌍 **World & Camera**
from .world.follow import Follow

# from .camera import Camera
# from .parallax import Parallax
# from .light import Light
# from .fog_of_war import FogOfWar

### 🧪 **AI & Navigation**
# from .ai_move_to import AIMoveTo
# from .pathfinder import Pathfinder
# from .vision import Vision
# from .behavior_tree import BehaviorTree

### 🚀 **Testing Components**
from .testers.movement_tester import MovementTester
from .testers.rotation_tester import RotationTester
from .testers.scale_tester import ScaleTester
