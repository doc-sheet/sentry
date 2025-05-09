import type {Relay, RelayActivity, RelaysByPublickey} from 'sentry/types/relay';

/**
 * Convert list of individual relay objects into a per-file summary grouped by publicKey
 */
export function getRelaysByPublicKey(relays: Relay[], relayActivities: RelayActivity[]) {
  return relays.reduce<RelaysByPublickey>((relaysByPublicKey, relay) => {
    const {name, description, created, publicKey} = relay;

    if (!relaysByPublicKey.hasOwnProperty(publicKey)) {
      relaysByPublicKey[publicKey] = {name, description, created, activities: []};
    }

    if (!relaysByPublicKey[publicKey]!.activities.length) {
      relaysByPublicKey[publicKey]!.activities = relayActivities.filter(
        activity => activity.publicKey === publicKey
      );
    }

    return relaysByPublicKey;
  }, {});
}
