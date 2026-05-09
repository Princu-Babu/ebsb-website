import re

def fix_team():
    with open('team.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove the display: none; from member-socials
    html = re.sub(r'\.member-socials\s*\{\s*display:\s*none;\s*\}', '', html)

    # 2. Fix the missing closing tags before Core Team
    # Find:
    #         </div>
    # 
    #   <!-- Core Team -->
    html = html.replace(
        '        </div>\n\n  <!-- Core Team -->',
        '        </div>\n      </div>\n    </div>\n  </section>\n\n  <!-- Core Team -->'
    )

    # 3. Delete the garbage team-poster divs
    # Find everything from <div class="team-poster to the end of the grid </div>
    html = re.sub(r'        <div class="team-poster slide-up.*?(?=      </div>\n    </div>\n  </section>\n\n  <!-- Footer -->)', '', html, flags=re.DOTALL)

    # 4. Add the LinkedIn links
    links = {
        'Pankaj Meena': 'https://www.linkedin.com/in/pankajkumarmeena?utm_source=share_via&utm_content=profile&utm_medium=member_android',
        'Kedar Choudhary': 'https://www.linkedin.com/in/kedar-choudhary-742498321?utm_source=share_via&utm_content=profile&utm_medium=member_android',
        'Moukthika': 'https://www.linkedin.com/in/moukthika-naidu-716101383?utm_source=share_via&utm_content=profile&utm_medium=member_android',
        'Aakanksha Garg': 'https://www.linkedin.com/in/bethegarg?utm_source=share_via&utm_content=profile&utm_medium=member_android',
        'Rahul Yadav': 'https://www.linkedin.com/in/rahul-yadav-840786320?utm_source=share_via&utm_content=profile&utm_medium=member_android',
        'Prateek Singh': 'https://www.linkedin.com/in/prateek-singh-106287348?utm_source=share_via&utm_content=profile&utm_medium=member_android',
        'Subrahmanyam': 'https://www.linkedin.com/in/subrahmanyam-machavolu-383163357?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app'
    }

    for name, link in links.items():
        # Find the block for the person
        # <h3 class="member-name">Name</h3>
        # ...
        # <a href="#"><i class="fa-brands fa-linkedin"></i></a>
        
        # We can use a regex to target the specific linkedin href for that name
        pattern = re.compile(rf'(<h3 class="member-name">{name}</h3>.*?<div class="member-socials">\s*<a href=")(#)("><i class="fa-brands fa-linkedin">)', re.DOTALL)
        html = pattern.sub(rf'\g<1>{link}\g<3>', html)

    with open('team.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done")

if __name__ == "__main__":
    fix_team()
