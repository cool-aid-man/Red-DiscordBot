########## SENSITIVE SECTION WARNING ###########
################################################
# Any edits of any of the exported names       #
# may result in a breaking change.             #
# Ensure no names are removed without warning. #
################################################

from .commands import (
    Cog as Cog,
    CogMixin as CogMixin,
    CogCommandMixin as CogCommandMixin,
    CogGroupMixin as CogGroupMixin,
    Command as Command,
    Group as Group,
    GroupCog as GroupCog,
    GroupMixin as GroupMixin,
    command as command,
    HybridCommand as HybridCommand,
    HybridGroup as HybridGroup,
    hybrid_command as hybrid_command,
    hybrid_group as hybrid_group,
    group as group,
    RedUnhandledAPI as RedUnhandledAPI,
    RESERVED_COMMAND_NAMES as RESERVED_COMMAND_NAMES,
)
from .context import Context as Context, GuildContext as GuildContext, DMContext as DMContext
from .converter import (
    DictConverter as DictConverter,
    RelativedeltaConverter as RelativedeltaConverter,
    TimedeltaConverter as TimedeltaConverter,
    finite_float as finite_float,
    get_dict_converter as get_dict_converter,
    get_timedelta_converter as get_timedelta_converter,
    parse_relativedelta as parse_relativedelta,
    parse_timedelta as parse_timedelta,
    positive_int as positive_int,
    NoParseOptional as NoParseOptional,
    UserInputOptional as UserInputOptional,
    RawUserIdConverter as RawUserIdConverter,
    CogConverter as CogConverter,
    CommandConverter as CommandConverter,
)
from .errors import (
    BotMissingPermissions as BotMissingPermissions,
    UserFeedbackCheckFailure as UserFeedbackCheckFailure,
    ArgParserFailure as ArgParserFailure,
)
from .help import (
    red_help as red_help,
    RedHelpFormatter as RedHelpFormatter,
    HelpSettings as HelpSettings,
)
from .requires import (
    CheckPredicate as CheckPredicate,
    GlobalPermissionModel as GlobalPermissionModel,
    GuildPermissionModel as GuildPermissionModel,
    PermissionModel as PermissionModel,
    PrivilegeLevel as PrivilegeLevel,
    PermState as PermState,
    Requires as Requires,
    permissions_check as permissions_check,
    bot_has_permissions as bot_has_permissions,
    bot_in_a_guild as bot_in_a_guild,
    bot_can_manage_channel as bot_can_manage_channel,
    bot_can_react as bot_can_react,
    has_permissions as has_permissions,
    can_manage_channel as can_manage_channel,
    has_guild_permissions as has_guild_permissions,
    is_owner as is_owner,
    guildowner as guildowner,
    guildowner_or_can_manage_channel as guildowner_or_can_manage_channel,
    guildowner_or_permissions as guildowner_or_permissions,
    admin as admin,
    admin_or_can_manage_channel as admin_or_can_manage_channel,
    admin_or_permissions as admin_or_permissions,
    mod as mod,
    mod_or_can_manage_channel as mod_or_can_manage_channel,
    mod_or_permissions as mod_or_permissions,
)

### DEP-WARN: Check this *every* discord.py update
from discord.ext.commands import (
    BadArgument as BadArgument,
    EmojiConverter as EmojiConverter,
    GuildConverter as GuildConverter,
    InvalidEndOfQuotedStringError as InvalidEndOfQuotedStringError,
    MemberConverter as MemberConverter,
    BotMissingRole as BotMissingRole,
    PrivateMessageOnly as PrivateMessageOnly,
    HelpCommand as HelpCommand,
    MinimalHelpCommand as MinimalHelpCommand,
    DisabledCommand as DisabledCommand,
    ExtensionFailed as ExtensionFailed,
    Bot as Bot,
    NotOwner as NotOwner,
    CategoryChannelConverter as CategoryChannelConverter,
    CogMeta as CogMeta,
    ConversionError as ConversionError,
    UserInputError as UserInputError,
    Converter as Converter,
    InviteConverter as InviteConverter,
    ExtensionError as ExtensionError,
    Cooldown as Cooldown,
    CheckFailure as CheckFailure,
    PartialMessageConverter as PartialMessageConverter,
    MessageConverter as MessageConverter,
    MissingPermissions as MissingPermissions,
    BadUnionArgument as BadUnionArgument,
    DefaultHelpCommand as DefaultHelpCommand,
    ExtensionNotFound as ExtensionNotFound,
    UserConverter as UserConverter,
    MissingRole as MissingRole,
    CommandOnCooldown as CommandOnCooldown,
    MissingAnyRole as MissingAnyRole,
    ExtensionNotLoaded as ExtensionNotLoaded,
    clean_content as clean_content,
    CooldownMapping as CooldownMapping,
    ArgumentParsingError as ArgumentParsingError,
    RoleConverter as RoleConverter,
    CommandError as CommandError,
    TextChannelConverter as TextChannelConverter,
    UnexpectedQuoteError as UnexpectedQuoteError,
    Paginator as Paginator,
    BucketType as BucketType,
    NoEntryPointError as NoEntryPointError,
    CommandInvokeError as CommandInvokeError,
    TooManyArguments as TooManyArguments,
    Greedy as Greedy,
    ExpectedClosingQuoteError as ExpectedClosingQuoteError,
    ColourConverter as ColourConverter,
    ColorConverter as ColorConverter,
    VoiceChannelConverter as VoiceChannelConverter,
    StageChannelConverter as StageChannelConverter,
    NSFWChannelRequired as NSFWChannelRequired,
    IDConverter as IDConverter,
    MissingRequiredArgument as MissingRequiredArgument,
    GameConverter as GameConverter,
    CommandNotFound as CommandNotFound,
    BotMissingAnyRole as BotMissingAnyRole,
    NoPrivateMessage as NoPrivateMessage,
    AutoShardedBot as AutoShardedBot,
    ExtensionAlreadyLoaded as ExtensionAlreadyLoaded,
    PartialEmojiConverter as PartialEmojiConverter,
    check_any as check_any,
    max_concurrency as max_concurrency,
    CheckAnyFailure as CheckAnyFailure,
    MaxConcurrency as MaxConcurrency,
    MaxConcurrencyReached as MaxConcurrencyReached,
    bot_has_guild_permissions as bot_has_guild_permissions,
    CommandRegistrationError as CommandRegistrationError,
    GuildNotFound as GuildNotFound,
    MessageNotFound as MessageNotFound,
    MemberNotFound as MemberNotFound,
    UserNotFound as UserNotFound,
    ChannelNotFound as ChannelNotFound,
    ChannelNotReadable as ChannelNotReadable,
    BadColourArgument as BadColourArgument,
    RoleNotFound as RoleNotFound,
    BadInviteArgument as BadInviteArgument,
    EmojiNotFound as EmojiNotFound,
    PartialEmojiConversionFailure as PartialEmojiConversionFailure,
    BadBoolArgument as BadBoolArgument,
    TooManyFlags as TooManyFlags,
    MissingRequiredFlag as MissingRequiredFlag,
    flag as flag,
    FlagError as FlagError,
    ObjectNotFound as ObjectNotFound,
    GuildStickerNotFound as GuildStickerNotFound,
    ThreadNotFound as ThreadNotFound,
    GuildChannelConverter as GuildChannelConverter,
    run_converters as run_converters,
    Flag as Flag,
    BadFlagArgument as BadFlagArgument,
    BadColorArgument as BadColorArgument,
    dynamic_cooldown as dynamic_cooldown,
    BadLiteralArgument as BadLiteralArgument,
    DynamicCooldownMapping as DynamicCooldownMapping,
    ThreadConverter as ThreadConverter,
    GuildStickerConverter as GuildStickerConverter,
    ObjectConverter as ObjectConverter,
    FlagConverter as FlagConverter,
    MissingFlagArgument as MissingFlagArgument,
    ScheduledEventConverter as ScheduledEventConverter,
    ScheduledEventNotFound as ScheduledEventNotFound,
    check as check,
    guild_only as guild_only,
    cooldown as cooldown,
    dm_only as dm_only,
    is_nsfw as is_nsfw,
    has_role as has_role,
    has_any_role as has_any_role,
    bot_has_role as bot_has_role,
    when_mentioned_or as when_mentioned_or,
    when_mentioned as when_mentioned,
    bot_has_any_role as bot_has_any_role,
    before_invoke as before_invoke,
    after_invoke as after_invoke,
    CurrentChannel as CurrentChannel,
    Author as Author,
    param as param,
    MissingRequiredAttachment as MissingRequiredAttachment,
    Parameter as Parameter,
    ForumChannelConverter as ForumChannelConverter,
    CurrentGuild as CurrentGuild,
    Range as Range,
    RangeError as RangeError,
    parameter as parameter,
    HybridCommandError as HybridCommandError,
    SoundboardSoundConverter as SoundboardSoundConverter,
    SoundboardSoundNotFound as SoundboardSoundNotFound,
)

__all__ = (
    "Cog",
    "CogMixin",
    "CogCommandMixin",
    "CogGroupMixin",
    "Command",
    "Group",
    "GroupCog",
    "GroupMixin",
    "command",
    "HybridCommand",
    "HybridGroup",
    "hybrid_command",
    "hybrid_group",
    "group",
    "RedUnhandledAPI",
    "RESERVED_COMMAND_NAMES",
    "Context",
    "GuildContext",
    "DMContext",
    "DictConverter",
    "RelativedeltaConverter",
    "TimedeltaConverter",
    "get_dict_converter",
    "get_timedelta_converter",
    "parse_relativedelta",
    "parse_timedelta",
    "NoParseOptional",
    "UserInputOptional",
    "RawUserIdConverter",
    "CogConverter",
    "CommandConverter",
    "BotMissingPermissions",
    "UserFeedbackCheckFailure",
    "ArgParserFailure",
    "red_help",
    "RedHelpFormatter",
    "HelpSettings",
    "CheckPredicate",
    "GlobalPermissionModel",
    "GuildPermissionModel",
    "PermissionModel",
    "PrivilegeLevel",
    "PermState",
    "Requires",
    "permissions_check",
    "bot_has_permissions",
    "bot_in_a_guild",
    "bot_can_manage_channel",
    "bot_can_react",
    "has_permissions",
    "can_manage_channel",
    "has_guild_permissions",
    "is_owner",
    "guildowner",
    "guildowner_or_can_manage_channel",
    "guildowner_or_permissions",
    "admin",
    "admin_or_can_manage_channel",
    "admin_or_permissions",
    "mod",
    "mod_or_can_manage_channel",
    "mod_or_permissions",
    "BadArgument",
    "EmojiConverter",
    "GuildConverter",
    "InvalidEndOfQuotedStringError",
    "MemberConverter",
    "BotMissingRole",
    "PrivateMessageOnly",
    "HelpCommand",
    "MinimalHelpCommand",
    "DisabledCommand",
    "ExtensionFailed",
    "Bot",
    "NotOwner",
    "CategoryChannelConverter",
    "CogMeta",
    "ConversionError",
    "UserInputError",
    "Converter",
    "InviteConverter",
    "ExtensionError",
    "Cooldown",
    "CheckFailure",
    "PartialMessageConverter",
    "MessageConverter",
    "MissingPermissions",
    "BadUnionArgument",
    "DefaultHelpCommand",
    "ExtensionNotFound",
    "UserConverter",
    "MissingRole",
    "CommandOnCooldown",
    "MissingAnyRole",
    "ExtensionNotLoaded",
    "clean_content",
    "CooldownMapping",
    "ArgumentParsingError",
    "RoleConverter",
    "CommandError",
    "TextChannelConverter",
    "UnexpectedQuoteError",
    "Paginator",
    "BucketType",
    "NoEntryPointError",
    "CommandInvokeError",
    "TooManyArguments",
    "Greedy",
    "ExpectedClosingQuoteError",
    "ColourConverter",
    "ColorConverter",
    "VoiceChannelConverter",
    "StageChannelConverter",
    "NSFWChannelRequired",
    "IDConverter",
    "MissingRequiredArgument",
    "GameConverter",
    "CommandNotFound",
    "BotMissingAnyRole",
    "NoPrivateMessage",
    "AutoShardedBot",
    "ExtensionAlreadyLoaded",
    "PartialEmojiConverter",
    "check_any",
    "max_concurrency",
    "CheckAnyFailure",
    "MaxConcurrency",
    "MaxConcurrencyReached",
    "bot_has_guild_permissions",
    "CommandRegistrationError",
    "GuildNotFound",
    "MessageNotFound",
    "MemberNotFound",
    "UserNotFound",
    "ChannelNotFound",
    "ChannelNotReadable",
    "BadColourArgument",
    "RoleNotFound",
    "BadInviteArgument",
    "EmojiNotFound",
    "PartialEmojiConversionFailure",
    "BadBoolArgument",
    "TooManyFlags",
    "MissingRequiredFlag",
    "flag",
    "FlagError",
    "ObjectNotFound",
    "GuildStickerNotFound",
    "ThreadNotFound",
    "GuildChannelConverter",
    "run_converters",
    "Flag",
    "BadFlagArgument",
    "BadColorArgument",
    "dynamic_cooldown",
    "BadLiteralArgument",
    "DynamicCooldownMapping",
    "ThreadConverter",
    "GuildStickerConverter",
    "ObjectConverter",
    "FlagConverter",
    "MissingFlagArgument",
    "ScheduledEventConverter",
    "ScheduledEventNotFound",
    "check",
    "guild_only",
    "cooldown",
    "dm_only",
    "is_nsfw",
    "has_role",
    "has_any_role",
    "bot_has_role",
    "when_mentioned_or",
    "when_mentioned",
    "bot_has_any_role",
    "before_invoke",
    "after_invoke",
    "CurrentChannel",
    "Author",
    "param",
    "MissingRequiredAttachment",
    "Parameter",
    "ForumChannelConverter",
    "CurrentGuild",
    "Range",
    "RangeError",
    "parameter",
    "HybridCommandError",
    "SoundboardSoundConverter",
    "SoundboardSoundNotFound",
)
