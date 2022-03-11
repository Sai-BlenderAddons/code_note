# browser setting override

class OverrideFileBrowserSettingsProperties(PropertyGroup):
    """Add-on Properties"""

    override = bpy.props.BoolProperty(
        name="Override Display Settings",
        default=True
        )

    display_type = bpy.props.EnumProperty(
        name="Display Mode",
        items=(('LIST_SHORT', 'Short List', 'Display Short List', 'SHORTDISPLAY', 0),
               ('LIST_LONG', 'Long List', 'Display Short List', 'LONGDISPLAY', 1),
               ('THUMBNAIL', 'Thumbnails', 'Display Thumbnails', 'IMGDISPLAY', 2)),
        default='THUMBNAIL'
        )

    sort_method = bpy.props.EnumProperty(
        name="Sort Method",
        items=(('FILE_SORT_ALPHA', "Name", 'Sort by Name', 'SORTALPHA', 0),
               ('FILE_SORT_EXTENSION', "Extension", 'Sort by Name Extension', 'SORTBYEXT', 1),
               ('FILE_SORT_TIME', "Date", 'Sort by Date', 'SORTTIME', 2),
               ('FILE_SORT_SIZE', "Size", 'Sort by Size', 'SORTSIZE', 3)),
        default='FILE_SORT_TIME'
        )

    display_size = bpy.props.EnumProperty(
        name="Display Size",
        items=(('TINY', "Tiny", 'Tiny Items', 0),
               ('SMALL', "Small", 'Small Items', 1),
               ('NORMAL', "Normal", 'Normal Items', 2),
               ('LARGE', "Large", 'Large Items', 3)),
        default='TINY'
        )