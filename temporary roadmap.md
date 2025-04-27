-   [ ] Collision with tiles/objects
-   [ ] Interaction prompt for objects/NPCs
-   [ ] Zone system (e.g. dock, hut, forest)
-   [ ] Tile/object metadata system
-   [ ] Items with ID, tags, and properties
-   [ ] Behaviors (edible, cookable, tradeable, etc.)
-   [ ] Item metadata storage (JSON)
-   [ ] Grid layout UI
-   [ ] Add/remove items, stackable support
-   [ ] Context actions (drop, use, cook, inspect)
-   [ ] Save player state, inventory, day, flags
-   [ ] Load on boot or from main menu
-   [ ] Cast rod, wait, catch system
-   [ ] Bait, rod type, weather/time influence
-   [ ] Loot tables for fish/junk/etc.
-   [ ] Input multiple ingredients
-   [ ] Recipe/mix-result output
-   [ ] Nutrition or status effects
-   [ ] Energy drains from actions
-   [ ] Hunger drains over time or days
-   [ ] Penalties (slower speed, blackouts, death)
-   [ ] Triggers next day
-   [ ] Resets energy
-   [ ] Hooks into dream system
-   [ ] In-game time tracking
-   [ ] Visual lighting shifts
-   [ ] Events based on time
-   [ ] Random or triggered weather
-   [ ] Fog, rain, thunder, sun
-   [ ] Impact on fishing, mood, dreams
-   [ ] Dream triggers from sleep + conditions
-   [ ] Random or story-based dream scenes
-   [ ] Dream memory tracking
-   [ ] Clock, weather icon, hunger/energy meters
-   [ ] Inventory access, fishing/cooking UIs
-   [ ] Cutscene/dialogue boxes
-   [ ] Scripted movements, dialogue, animations
-   [ ] Triggered by events, dreams, item use
-   [ ] NPCs with name, inventory, behavior
-   [ ] Dialogue system
-   [ ] Bartering / coin system
-   [ ] Triggers (day count, item found, dream seen)
-   [ ] Script execution (spawn item, run cutscene)
-   [ ] Increases with glitches, rare events
-   [ ] Alters dreams, fish behavior, weather
-   [ ] Fake movement to other islands
-   [ ] Fog + map swap logic
-   [ ] Seamless “teleporting” of environments
-   [ ] Collectible memory clues
-   [ ] Interactive wall to view story pieces
-   [ ] Link fragments to reveal bigger truths
-   [ ] Journal with active tasks/goals
-   [ ] NPC requests, unlockables, milestones
-   [ ] Ambient sounds, BGM, weather SFX
-   [ ] Audio triggers from events/dreams
-   [ ] Dome monitors player and adjusts world
-   [ ] Can be tied to suspicion or difficulty

2. **📐 Basic Collision System**

    - `BoxCollider` or `CircleCollider` component
    - Simple collision check in system (for testing, AABB is enough)
    - `CollisionTester` component for debugging

3. **🎥 Camera System (viewport transform)**

    - Camera should define the visible window (render offset)
    - Add zoom and smooth following

4. **🔧 Component Update System**
    - Each component can define an `update()` method
    - Run `update()` on all components if present
    - You can add tags like `UpdatableComponent` to mark them if needed

---

## 🔹 Phase 2 – Game Object Systems

5. **🎣 Fishing System (Start prototype)**

    - Simple fishing zone
    - Cast line, wait, get random item
    - Show UI prompt, sprite, animation

6. **🎒 Inventory System**

    - Item pickup/add/remove
    - Inventory slots with stacking
    - Later: item tooltips, drag/drop

7. **🖼 Animation System**

    - `Animator` component
    - Load sprite sheets + frame timings
    - Control playback (play/stop/set frame)

8. **🧭 Scene Transitions / Multiple Areas**
    - Trigger to change scenes (e.g., dock to another island)
    - Smooth fade transitions

---

## 🔹 Phase 3 – Simulation

9. **🌤 Environment System**

    - Day/night cycle
    - Dynamic weather system (rain, fog, etc.)

10. **🛌 Sleep / Dream System**

    - Advance time
    - Dream triggers
    - Possibly surreal cutscenes

11. **📋 Cutscene System**

    - Timeline-based
    - Trigger actions, movement, dialogue

12. **🧠 AI System (for fish or other NPCs later)**
    - FSM (Finite State Machine) or behavior trees

---

## 🧠 Bonus/Optional Utilities

-   🎨 Debug overlay (FPS, hitboxes, object count)
-   🧰 Developer console (basic input for debugging in runtime)
-   🔁 Undo/redo system for map editor
-   🔄 Serialization helpers for runtime save/load state

"""
