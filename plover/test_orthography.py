# Copyright (c) 2013 Hesky Fisher
# See LICENSE.txt for details.

from plover.orthography import add_suffix
import unittest

class OrthographyTestCase(unittest.TestCase):

    def test_add_suffix(self):
        cases = (
        
            ('artistic', 'ly', 'artistically'),
            ('cosmetic', 'ly', 'cosmetically'),
            ('establish', 's', 'establishes'),
            ('speech', 's', 'speeches'),
            ('approach', 's', 'approaches'),
            ('beach', 's', 'beaches'),
            ('arch', 's', 'arches'),
            ('larch', 's', 'larches'),
            ('march', 's', 'marches'),
            ('search', 's', 'searches'),
            ('starch', 's', 'starches'),
            ('stomach', 's', 'stomachs'),
            ('monarch', 's', 'monarchs'),
            ('patriarch', 's', 'patriarchs'),
            ('oligarch', 's', 'oligarchs'),
            ('cherry', 's', 'cherries'),
            ('day', 's', 'days'),
            ('penny', 's', 'pennies'),
            ('pharmacy', 'ist', 'pharmacist'),
            ('melody', 'ist', 'melodist'),
            ('pacify', 'ist', 'pacifist'),
            ('geology', 'ist', 'geologist'),
            ('metallurgy', 'ist', 'metallurgist'),
            ('anarchy', 'ist', 'anarchist'),
            ('monopoly', 'ist', 'monopolist'),
            ('alchemy', 'ist', 'alchemist'),
            ('botany', 'ist', 'botanist'),
            ('therapy', 'ist', 'therapist'),
            ('theory', 'ist', 'theorist'),
            ('psychiatry', 'ist', 'psychiatrist'),
            ('lobby', 'ist', 'lobbyist'),
            ('hobby', 'ist', 'hobbyist'),
            ('copy', 'ist', 'copyist'),
            ('beauty', 'ful', 'beautiful'),
            ('weary', 'ness', 'weariness'),
            ('weary', 'some', 'wearisome'),
            ('lonely', 'ness', 'loneliness'),
            ('narrate', 'ing', 'narrating'),
            ('narrate', 'or', 'narrator'),
            ('generalize', 'ability', 'generalizability'),
            ('reproduce', 'able', 'reproducible'),
            ('grade', 'ations', 'gradations'),
            ('urine', 'ary', 'urinary'),
            ('achieve', 'able', 'achievable'),
            ('polarize', 'ation', 'polarization'),
            ('done', 'or', 'donor'),
            ('analyze', 'ed', 'analyzed'),
            ('narrate', 'ing', 'narrating'),
            ('believe', 'able', 'believable'),
            ('animate', 'ors', 'animators'),
            ('discontinue', 'ation', 'discontinuation'),
            ('innovate', 'ive', 'innovative'),
            ('future', 'ists', 'futurists'),
            ('illustrate', 'or', 'illustrator'),
            ('emerge', 'ent', 'emergent'),
            ('equip', 'ed', 'equipped'),
            ('defer', 'ed', 'deferred'),
            ('defer', 'er', 'deferrer'),
            ('defer', 'ing', 'deferring'),
            ('pigment', 'ed', 'pigmented'),
            ('refer', 'ed', 'referred'),
            ('fix', 'ed', 'fixed'),
            ('alter', 'ed', 'altered'),
            ('interpret', 'ing', 'interpreting'),
            ('wonder', 'ing', 'wondering'),
            ('target', 'ing', 'targeting'),
            ('limit', 'er', 'limiter'),
            ('maneuver', 'ing', 'maneuvering'),
            ('monitor', 'ing', 'monitoring'),
            ('color', 'ing', 'coloring'),
            ('inhibit', 'ing', 'inhibiting'),
            ('master', 'ed', 'mastered'),
            ('target', 'ing', 'targeting'),
            ('fix', 'ed', 'fixed'),
            ('scrap', 'y', 'scrappy'),
            ('trip', 's', 'trips'),
            ('equip', 's', 'equips'),
            ('bat', 'en', 'batten'),
            ('smite', 'en', 'smitten'),
            ('got', 'en', 'gotten'),
            ('bite', 'en', 'bitten'),
            ('write', 'en', 'written'),
            ('flax', 'en', 'flaxen'),
            ('wax', 'en', 'waxen'),
            ('fast', 'est', 'fastest'),
            ('white', 'er', 'whiter'),
            ('crap', 'y', 'crappy'),
            ('lad', 'er', 'ladder'),
            ('translucent', 'cy', 'translucency'),
            ('bankrupt', 'cy', 'bankruptcy'),
            ('inadequate', 'cy', 'inadequacy'),
            ('secret', 'cy', 'secrecy'),
            ('impolite', 'cy', 'impolicy'),
            ('idiot', 'cy', 'idiocy'),
            ('free', 'ed', 'freed'),
            ('free', 'er', 'freer'),
            ('regulate', 'ry', 'regulatory'),
            
        )
        
        failed = []
        for word, suffix, expected in cases:
            if add_suffix(word, suffix) != expected:
                failed.append((word, suffix, expected))
                
        for word, suffix, expected in failed:
            print 'add_suffix(%s, %s) is %s not %s' % (word, suffix, add_suffix(word, suffix),expected)
            
        self.assertEqual(len(failed), 0)
        
if __name__ == '__main__':
    unittest.main()
