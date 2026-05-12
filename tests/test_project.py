def demo_museum_night():
    print("Moonlight Museum After Dark")

    artifacts = [
        Artifact(40, "Cursed Mirror", "mirror", 220, "North Hall"),
        Artifact(20, "Clockwork Bird", "machine", 80, "Workshop"),
        Artifact(60, "Whispering Map", "paper", 140, "Archive"),
        Artifact(10, "Glowing Key", "metal", 35, "Vault"),
        Artifact(30, "Moon Dial", "device", 120, "North Hall"),
        Artifact(50, "Silver Mask", "costume", 160, "Gallery"),
        Artifact(70, "Lantern Jar", "glass", 60, "Gallery"),
        Artifact(25, "Ink Compass", "device", 120, "Archive"),
    ]

    # ==========================================
    # BST
    # ==========================================

    bst = ArtifactBST()

    for artifact in artifacts:
        bst.insert(artifact)

    print("Inorder IDs:")
    print(bst.inorder_ids())

    # ==========================================
    # Queue
    # ==========================================

    queue = RestorationQueue()

    request1 = RestorationRequest(40, "Polish cracked frame")
    request2 = RestorationRequest(20, "Oil the wing gears")

    queue.add_request(request1)
    queue.add_request(request2)

    print("Next restoration request:")
    print(queue.peek_next_request())

    # ==========================================
    # Stack
    # ==========================================

    stack = ArchiveUndoStack()

    stack.push_action("Moved Lantern Jar to East Wing")
    stack.push_action("Archived Silver Mask")

    print("Undo action:")
    print(stack.undo_last_action())

    # ==========================================
    # Exhibit Route
    # ==========================================

    route = ExhibitRoute()

    route.add_stop("Entrance")
    route.add_stop("East Wing")
    route.add_stop("Basement")

    print("Exhibit route:")
    print(route.list_stops())

    # ==========================================
    # Reports
    # ==========================================

    print("Category counts:")
    print(count_artifacts_by_category(artifacts))